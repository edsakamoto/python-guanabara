# refaca o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado: EQUILATERO = todos os lados iguais; ISOSCELES - dois lados iguais e um diferete; ESCALENO - todos os lados diferentes
n1 = float(input('Digite um lado do triangulo: '))
n2 = float(input('Digite o segundo lado do triangulo: '))
n3 = float(input('Digite o terceiro lado do triangulo: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('-'*40)
    print('Os lados digitados podem formar um triangulo ',end='')    
    if n1 == n2 and n1 == n3:
        print('EQUILATERO')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISOSCELES')    
else:
    print('Os lados digitados não podem formar um triangulo')

