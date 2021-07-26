# crie um programa onde o ususario possa digitar varios valores numericos e cadastre-os em uma lista. caso o numero ja exista la dentro, ele nao sera adicionado. no final serao exibidos todos os valores unicos digitados, em ordem crescente.


x = list()

while True:
    n = int(input('Cadastre um número: '))
    if n not in x:
        x.append(n)
        print(f'Número {n} adicionado com sucesso!')
    else:
        print('Valor duplicado')
    continua = str(input('Continua [S/N] ? ')).strip().upper()
    if continua == 'N':
        break  
x.sort()      
print(f'Os valores adicionados foram {x}')


