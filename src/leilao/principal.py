from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

julia = Usuario("Julia")
pedro = Usuario("Pedro")

lance_da_julia = Lance(julia, 1000)
lance_do_pedro = Lance(pedro, 1001)

leilao = Leilao("Celular")

leilao.lances.append(lance_da_julia)
leilao.lances.append(lance_do_pedro)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu o lance {lance.valor}')

avaliador = Avaliador()

avaliador.avalia(leilao)
print(f'Menor lance: {avaliador.menor_lance} \nMaior lance: {avaliador.maior_lance}')