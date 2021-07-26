""" crie uma tupla preenchida com os 20 primeiros colocados ta tabela do campeonato brasileiro de futebol na ordem de colocacao, depois mostre:
a) os 5 primeiros colocados
b) os ultimos 4 colocados
c) os times em ordem alfabetica
d) em que posicao esta o time da chapecoense
"""

brasileirao = ('Flamengo','Internacional','Atlético-MG','São Paulo','Fluminense','Grêmio','Palmeiras','Santos','Athletico-PR','Bragantino','Ceará SC','Corinthians','Atlético-GO','Chapecoense','Sport Recife','Fortaleza','Vasco da gama','Goiás','Coritiba','Bota fogo')

"""
teste = len(brasileirao[:-1])
teste2 = len(brasileirao)-1
print(teste, teste2)
"""
print('*-'*30)
#for c in range(0,len(brasileirao[:5])):
#    print(f'O {c+1}º colocado é o {brasileirao[c]}')
print(f'Os 5 primeiros são {brasileirao[0:5]}')
print('*-'*30)
#for c in range(len(brasileirao[4:-1]),len(brasileirao[:-1])+1):
#    print(f'O {c+1}º colocado é o {brasileirao[c]}')
print(f'Os 4 últimos são {brasileirao[-4:]}')
print('*-'*30)
print('Ordem alfabética: ', end='')
print(sorted(brasileirao))
print('*-'*30)
#for c in brasileirao:
#    if 'Chapecoense' in c:
#        print(c,brasileirao)
print(f'O Chapecoense está na {brasileirao.index("Chapecoense") + 1}º posicao')