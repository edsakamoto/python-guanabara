# crie um programa que leia duas notas de um aluno e calcule a sua media, mostrando uma mensagem no final, de acordo com a media atingida. media abaixo de 5: reprovado; media entre 5 e 6.9: recuperacao; media 7 ou acima: aprovado

nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
media = (nota1 + nota2) / 2
#if media >=5 and media <= 6.9:
if 7 > media >= 5:
    print('RECUPERACAO! Nota média: {:.1f}'.format(media))
elif media < 5:
    print('REPROVADO! Nota média: {:.1f}'.format(media)) 
else:
    print('APROVADO! Nota média: {:.1f}'.format(media))