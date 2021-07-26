"""
Aula 17

Variáveis compostos: tuplas, LISTAS, dicionarios

Listas são mutáveis, diferente das tuplas que são imutáveis.
tuplas = () -> definido por parenteses
listas = [] -> definido por colchetes

"""

"""
num = [2, 5, 9, 1]
num[2] = 3 # altera a posicao 2 (valor 9) para o valor 3
num.append(7) #adiciona o numero 7 na lista
num.sort(reverse=True)
num.insert(2, 2)
#num.pop(2)
num.remove(2)
print(num)
print(f'essa lista tem {len(num)} elementos.')
"""
"""
valores = list()
#valores.append(5)
#valores.append(9)
#valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v} ! ')
print('Cheguei ao final da lista')
"""

a = [2, 3, 4, 7]
b = a # nesse formato não realiza uma copia da lista "a", está simplesmente linkando a variavel b para a, e o resultado é que se eu alterar alguma coisa na "b", a alteração irá refletir na "a" e vice-versa
b[2] = 8
c = b[:] # neste formato eu realizo uma copia da lista 'b' e consequentemente consigo realizar alterações na lista 'c' sem alterar as outras listas.
c[2] = 4
print(f'lista A: {a}')
print(f'lista B: {b}')
print(f'lista c: {c}')