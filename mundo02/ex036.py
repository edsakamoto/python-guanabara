# criar um programa para aprovar um empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Digite o valor da casa que deseja simular o empréstimo bancário: R$ '))
rendaMensal = float(input('Digite o valor da sua renda mensal: R$ '))
tempo = int(input('Em quanto tempo anos você quer quitar o empréstimo? '))
limite = 0.3
if rendaMensal * limite < valorCasa / (tempo * 12):
    print('A prestação excede o limite de 30 por cento da renda mensal!')
else:
    print('Empréstimo aprovado! {:.2f} de prestação mensal'.format(valorCasa / (tempo * 12)))    

