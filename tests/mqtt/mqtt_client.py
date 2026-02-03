import time
import threading
import queue
import ssl
import paho.mqtt.client as mqtt


class MqttClient:
    """
    MQTT client support for Behave.
    Handles connection, publish, subscribe, and message buffering.
    """

    def __init__(self, broker, port=1883, client_id=None, use_tls=False):
        client_id = str(client_id) if client_id else f"behave-{threading.get_ident()}"

        try:

            # Usa callback_api_version v1 per compatibilità semplice
            self.client = mqtt.Client(
                client_id=client_id,
                protocol=mqtt.MQTTv311,
            )
        except Exception as e:  # <- qui catturi l'eccezione
            print(f"Errore creando il client MQTT: {e}")
        self.broker = broker
        self.port = port
        self.received_messages = {}  # {topic: last payload}
        self._queue = queue.Queue()
        self._connected_event = threading.Event()

        # TLS se richiesto
        if use_tls:
            self.client.tls_set(cert_reqs=ssl.CERT_NONE)
            self.client.tls_insecure_set(True)

        # Callback
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message

    # ----------------------------
    # Callbacks
    # ----------------------------
    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            try:
                self._connected_event.set()
            except Exception as e:  # <- qui catturi l'eccezione
                print(f"Errore creando il client MQTT: {e}")

        else:
            raise ConnectionError(f"MQTT connection failed with code {rc}")

    def _on_message(self, client, userdata, msg):
        try:
            payload = msg.payload.decode()
        except UnicodeDecodeError:
            payload = msg.payload
        self.received_messages[msg.topic] = payload
        self._queue.put({"topic": msg.topic, "payload": payload})

    # ----------------------------
    # Connection management
    # ----------------------------
    def connect(self, timeout=10):
        self.client.connect(self.broker, self.port)
        self.client.loop_start()
        if not self._connected_event.wait(timeout):
            raise TimeoutError(f"Could not connect to broker {self.broker}:{self.port}")

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

    # ----------------------------
    # Publish / Subscribe
    # ----------------------------
    def subscribe(self, topic, qos=0):
        self.client.subscribe(topic, qos)

    def unsubscribe(self, topic):
        self.client.unsubscribe(topic)

    def publish(self, topic, message, qos=0, retain=False):
        info = self.client.publish(topic, message, qos, retain)
        info.wait_for_publish()

    # ----------------------------
    # Listen for messages
    # ----------------------------
    def wait_for_message(self, topic, timeout=5):
        """
        Wait for a message on a topic. Returns the payload.
        """
        end_time = time.time() + timeout

        # Check buffered messages first
        if topic in self.received_messages:
            return self.received_messages.pop(topic)

        while time.time() < end_time:
            try:
                msg = self._queue.get(timeout=end_time - time.time())
                if msg["topic"] == topic:
                    return msg["payload"]
            except queue.Empty:
                pass

        raise TimeoutError(f"No message received on topic '{topic}' within {timeout}s")
