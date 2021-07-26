#escreve um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar RS7,00 por cada km acima do limite.

velocidade_atual = float(input('Qual é a velocidade atual do veículo em km/h: '))

if velocidade_atual > 80:
    print('velocidade acima do limite permitido. Condutor será multado em R${:.2f} !'.format((velocidade_atual - 80) * 7))
else:
    print('Parabéns, continue assim, respeitando o limite de velocidade!')
