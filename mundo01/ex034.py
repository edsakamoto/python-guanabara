#escreve um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. para salarios superios a 1250, calcule um aumento de 10% . Para os inferiores ou iguais o aumento é de 15%

salario = float(input('Informe o salário: '))
if salario > 1250:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.15
print('O novo salário é: R${:.2f}'.format(novo_salario))