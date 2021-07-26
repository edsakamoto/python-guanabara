# programar um jogo de jankempo
from random import choice
from time import sleep
adversario = int(input('''
[1] PAPEL 
[2] PEDRA
[3] TESOURA 
------------------------------------------
DIGITE O NÚMERO DA SUA JOGADA DE JOKEMPO: '''))

print('Jo')
sleep(1)
print('Kem')
sleep(1)
print('Po')
computador = [1,2,3]
jogada_computador = choice(computador)
#jogada_computador = 1
if adversario == jogada_computador:
    print('EMPATE!')
elif adversario == 1 and jogada_computador == 2:
    print('Você VENCEU!')
elif adversario == 1 and jogada_computador == 3:
    print('Você PERDEU!')
elif adversario == 2 and jogada_computador == 1:
    print('Você PERDEU!')
elif adversario == 2 and jogada_computador == 3:
    print('Você VENCEU!')
elif adversario == 3 and jogada_computador == 1:
    print('Você VENCEU!')
elif adversario == 3 and jogada_computador == 2:
    print('Você PERDEU!')
else:
    print('Opção digitada fora das opções disponíveis. Tente novamente.')


