Feature: Somma semplice

  Scenario Outline: sommare due numeri
    Given ho il numero <a>
    And ho il numero <b>
    When li sommo
    Then il risultato è <risultato>

    Examples:
      | a | b | risultato |
      | 2 | 3 | 5         |
      | 1 | 4 | 5         |
      | 0 | 0 | 0         |
