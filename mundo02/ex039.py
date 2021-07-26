# leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao seviço militar, se é a hora exta de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date, datetime

'''hoje = date.today()
agora = datetime.now()
print(hoje - date(year= 1991,month=12, day=11) / 365)'''
#print(agora - 1991)
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
alistamento = 18
if idade == alistamento:
    print('Você precisa se alistar imediatamente!')
elif idade > alistamento:
    print('Você já deveria ter se alistado a {} anos atras'.format(idade - alistamento))
else:
    print('Você ainda não tem idade para se alistar, faltam ainda {} anos.'.format(alistamento - idade))
