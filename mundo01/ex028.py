#escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

import random as r
numero = [0,1,2,3,4,5]

random = r.choice(numero)
#print(random)
x = int(input('O robo escolheu um numero entre 0 a 5, tenta advinhar! '))
if x == random:
    print('Parabéns, você acertou! {} foi o número escolhido pelo robô e você digitou {}'.format(random,x))
else:
    print('Putz o número escolhido: {} , é diferente do que foi escolhido pelo robô: {} !'.format(x,random))

