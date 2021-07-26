# faça um programa que leia 5 valores numericos e guarde-os em uma lista. no final mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista

lista = list()
mai = 0
men = 0
for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
#for pos, val in enumerate(lista):
    #print(pos, val)
#    print(f'O maior valor digitado é o {max(val)} que está na posição {lista.index(max(val))}')    
#    print(f'O menor valor digitado é o {min(val)} que está na posição {lista.index(min(val))}')
print(lista)    
#print(f'O maior valor digitado é o {max(lista)} que está na posição {lista.index(max(lista))+1}º ')    
#print(f'O maior valor digitado é o {min(lista)} que está na posição {lista.index(min(lista))+1}º ')  
print(f'O maior valor digitado foi {mai} nas posicoes ' , end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}... ', end='')
print()        
print(f'O menor valor digitado foi {men} nas posicoes ' , end='')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}... ', end='')