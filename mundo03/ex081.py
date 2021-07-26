""" 
crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso mostre:

a) quantos numeros foram digitados
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista
"""

numeros = list()
#contador = 0
tem5 = ''
while True:
    #x = int(input('Digite um número: '))
    #contador += 1
    numeros.append(int(input('Digite um número: ')))    
    continua = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if continua == 'N':
        break
print('*'*30)
print(f'Foram digitados {len(numeros)} numero(s)')
print()
numeros.sort(reverse=True)
print(f'Os numeros digitados de forma decrescente: {numeros}')
print()
if 5 in numeros:
    tem5 = 'SIM'
else:
    tem5 = 'NAO'
print(f'Na lista existe o número 5? {tem5}')
print()
print('*'*30)


    
    

