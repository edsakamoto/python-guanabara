# crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista, ja na posicao correta de insercao (sem usar o sort()). no final, mostre a lista ordenada na tela

numeros = list()
for n in range(0,5):
    x = int(input(f'Digite o {n+1} numero: '))
    tam = len(numeros)
    if n == 0 or n > numeros[-1]:
        numeros.append(x)
    else:
        pos = 0
        while pos < len(numeros):
            if x <= numeros[pos]:
                numeros.insert(pos, x)
                break
            pos +=1
print('-'*30)
print(f'Os valores digitados em ordem foram {numeros}')

    

"""
    if tam == 0:
        numeros.append(x)
    else:
        for pos, val in enumerate(numeros):
            if val > x:
                numeros.insert(pos,x)
            else:
                #numeros.insert(pos+1,x)
                print(numeros)
"""

