from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.julia = Usuario("Julia", 500.0)
        self.pedro = Usuario("Pedro", 500.0)

        self.lance_da_julia = Lance(self.julia, 1000)
        self.lance_do_pedro = Lance(self.pedro, 1001)

        self.leilao = Leilao("Celular")

    def test_deve_retornar_o_maior_e_menor_valor_de_um_lance_quando_colocado_em_ordem_crescente(self):

        self.leilao.propoe(self.lance_da_julia)
        self.leilao.propoe(self.lance_do_pedro)



        menor_valor_esperado = 1000
        maior_valor_esperado = 1001
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_menor_que_o_ultimo(self):

       with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_pedro)
            self.leilao.propoe(self.lance_da_julia)




    def test_deve_retornar_o_maior_e_menor_lance_quando_adicionado_3_lances(self):
        steven = Usuario("Steven", 500.0)
        lance_do_steven = Lance(steven, 20000)



        self.leilao.propoe(self.lance_da_julia)
        self.leilao.propoe(self.lance_do_pedro)
        self.leilao.propoe(lance_do_steven)


        menor_valor_esperado = 1000
        maior_valor_esperado = 20000
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    #se o leilao n tiver lances pode propor qualquer lance
    def test_deve_permitir_propor_caso_nao_haja_lances(self):
        self.leilao.propoe(self.lance_do_pedro)


        quantidade_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidade_lances)
    #se o ultimo usuario for diferente deve propor lances
    def test_deve_permitir_propor_caso_ultimo_usuario_seja_diferente(self):
        steven = Usuario("Steven", 500.0)
        lance_do_steven = Lance(steven, 20000)

        self.leilao.propoe(self.lance_da_julia)
        self.leilao.propoe(lance_do_steven)

        quantidade_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(2, quantidade_lances_recebidos)

    #se o ultimo usuario for o mesmo n deve permitir propor
    def test_nao_deve_permitir_propor_caso_ultimo_usuario_seja_o_mesmo(self):
        lance_ju200 = Lance(self.julia, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(lance_ju200)
            self.leilao.propoe(self.lance_da_julia)

