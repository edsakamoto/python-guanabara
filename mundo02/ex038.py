# escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem: O primeiro valor é maior / O segundo valor é maior OU Não existe valor maior, os dois são iguais

n1 = int(input('Digite um valor qualquer: '))
n2 = int(input('Digite um outro valor qualquer: '))
print('-'*30)
print('COMPARANDO OS NUMEROS DIGITADOS')
print('-'*30)
if n1 > n2:
    print('O primeiro número digitado, {}, é MAIOR do que o Segundo número digitado, {}'.format(n1,n2))
elif n2 > n1:
    print('O primeiro número digitado, {}, é MENOR do que o Segundo número digitado, {}'.format(n1,n2))
else:
    print('Os números digitados são iguais!')

