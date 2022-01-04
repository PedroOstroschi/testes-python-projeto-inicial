from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def setUp(self):
        self.julia = Usuario("Julia")
        self.pedro = Usuario("Pedro")

        self.lance_da_julia = Lance(self.julia, 1000)
        self.lance_do_pedro = Lance(self.pedro, 1001)

        self.leilao = Leilao("Celular")

    def test_deve_retornar_o_maior_e_menor_valor_de_um_lance_quando_colocado_em_ordem_crescente(self):


        self.leilao.lances.append(self.lance_da_julia)
        self.leilao.lances.append(self.lance_do_pedro)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 1000
        maior_valor_esperado = 1001
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_menor_lance_quando_adicionado_3_lances(self):
        steven = Usuario("Steven")
        lance_do_steven = Lance(steven, 20000)

        leilao = Leilao("Celular")

        leilao.lances.append(self.lance_da_julia)
        leilao.lances.append(self.lance_do_pedro)
        leilao.lances.append(lance_do_steven)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 1000
        maior_valor_esperado = 20000
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)