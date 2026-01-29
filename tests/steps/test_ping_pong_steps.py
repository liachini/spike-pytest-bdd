import json
from pytest_bdd import given, when, then, scenario, parsers


# Collega il feature file
@scenario("ping_pong.feature", "Verify MQTT Ping Pong mechanism")
def test_mqtt_ping_pong():
    pass


# --- Steps ---
@given("I am connected to the MQTT broker")
def step_connected(mqtt_client):
    if not mqtt_client:
        raise RuntimeError("MQTT client not initialized")


@given('I am subscribed to topic "{topic}"')
@given(parsers.parse('I am subscribed to topic "{topic}"'))
def step_subscribe(mqtt_client, topic):
    mqtt_client.subscribe(topic)
    mqtt_client.subscribed_topic = topic


@when('I publish a ping message to topic "{topic}"')
@when(parsers.parse('I publish a ping message to topic "{topic}"'))
def step_publish(mqtt_client, topic):
    mqtt_client.publish(topic, json.dumps({"data": {"topic": topic}}))


@then('I should receive a pong message on topic "{topic}" within {timeout:d} seconds')
@then(
    parsers.parse(
        'I should receive a pong message on topic "{topic}" within {timeout:d} seconds'
    )
)
def step_wait_pong(mqtt_client, topic, timeout):
    payload = mqtt_client.wait_for_message(topic, timeout)
    assert payload is not None, f"No message received on topic {topic}"
