"""
crie um programa que leia nome e peso de varias pessoas, guardadndo tudo em uma lista.
no final mostre:
a) quantas pessoas foram cadastradas
b) uma listagem com as pessoas mais pesadas
c) uma listagem com as pessoas mais leves
"""

princ = list()
temp = list()
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp [1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar [s/n]? ')).upper().strip()
    if resp == 'N':
        break



print('-'*30)
print(f'Lista temp: {temp}')
print()
print(f'Lista das pessoas cadastradas: {princ}')
print()
print(f'Quantidade de pessoas cadastradas: {len(princ)}')
print()
print(f'O maior peso foi de {mai} kilos. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men} kilos. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')

