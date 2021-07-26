"""
crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectvamente. Ao final, mostre o conteudo das tres listas geradas

"""
numeros = []
par = []
impar = []
while True:
    x = int(input('Digite um numero: '))
    numeros.append(x)
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
    cont = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if cont == 'N':
        break
print('*'*30)
print()
print(f'A lista dos números digitados: {numeros}')
print()
print(f'Os numeros pares digitados na lista: {par}')
print()
print(f'Os numeros impares digitados na lista: {impar}')
print('*'*30)
