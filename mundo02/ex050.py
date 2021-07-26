# desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem PARES. Se o valor digitado for impar, desconsidere-o

soma = 0
for cont in range(1,7):
    n = int(input('Digite o {} numero: '.format(cont)))
    if n % 2 == 0:
        soma = soma + n
print('A soma dos pares digitados foram: {}'.format(soma))
