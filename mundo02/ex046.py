# faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles
from time import sleep
countdown = 10
for c in range(10,-1,-1):
    print('Faltam {} segundos para fireworks!'.format(c))
    #countdown = countdown - 1
    sleep(1)

print('BOOM!') 
