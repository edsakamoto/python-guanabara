#crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar
numero = int(input('digite um número: '))

if numero % 2 == 0:
    print('número digitado: {} é PAR'.format(numero))
else:
    print('número digitado: {} é ÍMPAR'.format(numero))
