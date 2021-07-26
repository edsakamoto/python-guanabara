# faca um programa que calcule a soma entre todos os numeros que sao multiplos de tres e que se encontram no intervalo de 1 ate 500
soma = 0
contador = 0
for c in range(1,501,2):
    if c % 3 == 0:
        #print(c,end=' ')
        soma = soma + c
        contador = contador + 1
print('A soma de todos os valores é {} e foram somadas {} números'.format(soma,contador))
