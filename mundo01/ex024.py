#crie um programa que leia o nome de uma cidade, diga se ela começa ou não com o nome Santo

cidade = str(input('digite o nome de uma cidade: ')).strip().upper()
lista = cidade.split()
procura = lista[0]
print(procura == 'SANTO')