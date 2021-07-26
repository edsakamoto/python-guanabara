# crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estão na tupla

import random 
num = (random.sample(range(0,100000),5))
ordenado = sorted(num)
print('-*'*30)
print(f'Os numeros sorteados são {num}')
print('-*'*30)
print(f'O menor valor sorteado foi {ordenado[0]} e o maior numero sorteado foi {ordenado[4]}!')

#jeito guanabara abaixo:
print('-'*30)
numeros = (random.randint(1,99999),random.randint(1,99999),random.randint(1,99999),random.randint(1,99999),random.randint(1,99999))
print('Os numeros sorteados foram: ', end='')
for c in numeros:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')


