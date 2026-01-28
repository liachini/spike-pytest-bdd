import pytest
from pytest_bdd import scenario, given, when, then, parsers


@scenario("../features/moltiplicazione.feature", "moltiplicare 2 numeri")
def test_moltiplicazione():
    pass


@pytest.fixture
def contesto():
    return {"numeri": []}


@given(parsers.parse("ho il numero {numero:d}"))
def ho_numero(contesto, numero):
    contesto["numeri"].append(numero)


@when("li moltiplico", target_fixture="risultato")
def moltiplica_numeri(contesto):
    res = 1
    for n in contesto["numeri"]:
        res *= n
    return res


@then(parsers.parse("il risultato è {atteso:d}"))
def verifica_risultato(risultato, atteso):
    assert risultato == atteso
