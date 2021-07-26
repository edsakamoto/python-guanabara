# faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. O programa será interrompido quando o numero solicitado for negativo
n = 0
#contador = 0
contador_tabuada = 0
#n = int(input('Digite o número da tabuada que gostaria de visualizar (digite numero negativo para sair): '))
print('-'*30)
while n >= 0:    
    n = int(input('Digite o número da tabuada que gostaria de visualizar (digite numero negativo para sair): '))
    print('-'*30)
    if n < 0:
        break        
    for c in range(0,11):
        print(f' {n} x {c} = {n*c}')     
    print('-'*30)
print('Fim')


