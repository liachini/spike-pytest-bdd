Feature: MQTT Ping Pong

  Scenario: Verify MQTT Ping Pong mechanism
    Given I am connected to the MQTT broker
    And I am subscribed to topic "toDevice/pong"
    When I publish a ping message to topic "toRabbit/ping"
    Then I should receive a pong message on topic "toDevice/pong" within 10 seconds
