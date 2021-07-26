# programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversao: 1 para binário, 2 para octal e 3 para hexadecimal

n = int(input('Digite um número qualquer: '))
base = int(input('Digite a base para conversão, 1 para binário, 2 para Octal e 3 para Hexadecimal: '))
if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n,bin(n)[2:])) # as duas primeiras casas não precisa mostrar.
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n,oct(n)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n,hex(n)[2:]))
else:
    print('Opção inválida, favor digitar um número entre 1 e 3')