"""
desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre: 
a) quantas vezes apareceuu o valor 9 
b) em que posicao foi digitado o primeiro valor 3. 
c) quais foram os numeros pares
"""

x = (int(input('Digite um numero:'))
    ,int(input('Digite o segundo numero:'))
    ,int(input('Digite o terceiro numero:'))
    ,int(input('Digite o ultimo numero:')))
#nove = x.count(9)
print('-'*30)
print(f'Os numeros digitados: {x}')
print('-'*30)
print(f'Apareceu o numero nove dentro da lista {x.count(9)} vezes')
print('-'*30)
if 3 in x:
    print(f'O valor 3 apareceu na {x.index(3)+1}º posicao')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('-'*30)
print('Os valores pares digitados foram ',end='')
for n in x:
    if n %  2 == 0:
        print(n, end=' ')
