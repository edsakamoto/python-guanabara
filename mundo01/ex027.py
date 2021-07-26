#um programa que leia o nome completo de uma pessoa, mostrando sem seguida o primeiro e o último nome separadamente

nome = str(input('Digite o seu nome completo: ')).strip()
sep_nome = nome.split()
print('nome digitado:' ,nome)
print('seu primeiro nome: {}'.format(sep_nome[0]))
print('seu ultimo nome: {}'.format(sep_nome[-1]))
