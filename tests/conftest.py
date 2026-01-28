import pytest
from support.mqtt_client import MqttClient

BROKER = "10.130.127.1"
PORT = 1883


@pytest.fixture(scope="module")
def mqtt_client():
    """Crea e connette il client MQTT"""
    client = MqttClient(BROKER, PORT)
    client.connect()
    yield client
    client.disconnect()
