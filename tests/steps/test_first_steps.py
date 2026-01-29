from pytest_bdd import scenario, given, when, then, parsers
import pytest


@scenario("first.feature", "sommare due numeri")
def test_sommare_due_numeri():
    pass


@pytest.fixture
def contesto():
    return {}


@given("ho il numero {numero}")
@given(parsers.parse("ho il numero {numero:d}"))
def aggiungi_numero(contesto, numero):
    contesto.setdefault("numeri", []).append(numero)


@when("li sommo", target_fixture="somma")
def somma(contesto):
    return sum(contesto["numeri"])


@then("il risultato è {risultato}")
@then(parsers.parse("il risultato è {risultato:d}"))
def risultato(somma, risultato):
    assert somma == risultato
