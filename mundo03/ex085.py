"""
crie um programa onde o usuario possa digitar sete valores numericos e cadastre os em uma lista unica que mantenha separados os valores pares e impares. no final mostre os valores pares e impares em ordem crescente
"""

num = [[],[]]
valor = 0

for c in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-'*30)
print(f'Numeros digitados: {valor} ')
num[0].sort()
num[1].sort()
print(f'Numeros digitados par: {num[0]} ')
print(f'Numeros digitados impar: {num[1]} ')
