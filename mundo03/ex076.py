"""
crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia. no final mostre uma listagem de preços, organizando os dados em forma tabular
"""
txt = 'Listagem de preços'
produtos = ('Lapis', 1.5, 'Borracha', 0.5, 'Caneta', 2.5, 'Rezma', 15, 'Caderno', 10)
print('-'*30)
print(txt.center(30))
print('-'*30)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')

