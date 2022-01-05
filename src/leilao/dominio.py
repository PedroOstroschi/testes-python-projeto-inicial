from src.leilao.excecoes import LanceInvalido

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self._valida_valor(valor):
            raise LanceInvalido('Não pode propor um lance com valor maior que o da carteira.')
        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def _valida_valor(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0
        self.menor_lance = 0

    def _tem_lances(self):
        return self.__lances

    def propoe(self, lance: Lance):
        if self.lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor
            self.__lances.append(lance)
        else:
            raise LanceInvalido("Erro ao propor lance.")

    @property
    def lances(self):
        return self.__lances[:]#copia rasa

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        else:
            raise LanceInvalido('O mesmo usuário não pode dar dois lances seguidos. ')

    def valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        else:
            raise LanceInvalido('O lance tem que ser maior que o anterior.')

    def lance_eh_valido(self, lance):
        not self._tem_lances() or (self._usuarios_diferentes(lance) and
                                          self.valor_maior_que_lance_anterior(lance))




