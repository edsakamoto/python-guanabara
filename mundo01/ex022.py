#programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiuculas e minusculas, quantas letras ao todo sem considerar espaços, quantas letras tem o primeiro nome

nome = input("digite um nome completo: ")
upper = nome.upper()
lower = nome.lower()
#print("nome em capslock: {}  e nome em lower: {} ".format(upper,lower))
tamanho = len(nome)
branco = nome.count(' ')
lista = nome.split()
tamPrimeiroNome = len(lista[0])
print(' nome em capslock: {} \n nome em lower: {} \n quantas letras ao todo sem considerar o espaço: {} \n quantas letras tem o primeiro nome: {} '.format(upper,lower,tamanho - branco,tamPrimeiroNome))
#spaces = nome.find(' ')
#print(spaces)
