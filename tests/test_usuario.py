from src.leilao.dominio import Usuario, Leilao
from src.leilao.excecoes import LanceInvalido
import pytest

@pytest.fixture
def pedro():
    return Usuario("Pedro", 56)

@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_do_usuario_quando_este_propor_um_lance(pedro, leilao):
    pedro.propoe_lance(leilao, 55.0)
    assert pedro.carteira == 1.0

def test_deve_permitir_propor_caso_valor_menor_que_a_carteira(pedro, leilao):
    pedro.propoe_lance(leilao, 55.0)
    assert pedro.carteira == 1.0

def test_deve_permitir_propor_quando_valor_igual_ao_da_carteira(pedro, leilao):
    pedro.propoe_lance(leilao, 56.0)
    assert pedro.carteira == 0.0

def test_nao_deve_permitir_propor_valor_maior_que_a_carteira(pedro, leilao):
    with pytest.raises(LanceInvalido):
        pedro.propoe_lance(leilao, 100.0)
        assert pedro.carteira == 56.0