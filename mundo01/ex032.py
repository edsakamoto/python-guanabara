#um programa que leia um ano qualquer e verifica se é ano bissexto ou não
from datetime import date
ano = int(input('digite o ano a ser analisado ou digite 0 para analisar o ano atual: '))

#div4 = ano % 4
#div100 = ano % 100
#div400 = ano % 400
#print('{} {} {}'.format(div4,div100,div400))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é ano Bissexto!'.format(ano))
else:
    print('{} não é ano Bissexto!'.format(ano))
    
