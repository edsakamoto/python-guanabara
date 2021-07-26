"""
crie um programa que tenha uma tupla com varias palavras (n usar acentos). depois disso, voce deve mostrar, para cada palavra, quais são as suas vogais
"""

palavras = ('laranja', 'pera', 'arnold', 'sweden')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
        