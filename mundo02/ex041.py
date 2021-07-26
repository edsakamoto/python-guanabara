# a confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos - Mirim ; até 14 anos - Infantil; até 19 anos - Júnior; Até 25 anos - Sênior; Acima de 25 anos: Master

from datetime import date
nascimento = int(input('Informe o ano de nascimento: '))
anoAtual = date.today().year

idade = anoAtual - nascimento
if idade <= 9:
    print('Idade atual: {} anos - Categoria MIRIM'.format(idade))
elif idade <= 14 :
    print('Idade atual: {} anos - Categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Idade atual: {} anos - Categoria JÚNIOR'.format(idade))
elif idade <= 25:
    print('Idade atual: {} anos - Categoria SÊNIOR'.format(idade))
else: 
    print('Idade atual {} anos - Categoria MASTER'.format(idade))



