# calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento. a vista em dinheiro ou cheque = 10% desconto; a vista no cartao = 5% desconto; em até 2x no cartao = preço normal; 3x ou mais no cartao = 20% de juros
prod = float(input('Digite o preço do produto: R$ '))
opcao = int(input(''' Opções disponíveis para pagamento: 
[1] para Dinheiro/Cheque
[2] para Cartão à Vista
[3] para 2x no Cartão
[4] para 3x ou Mais no Cartão
------------------------------
Selecione uma das opções: ''')) 
if opcao == 3:
    parcela = 2
    print('O valor total do produto será R${:.2f} e será dividio em {} vezes que resultará em parcelas de R$ {:.2f}'.format(prod, parcela, prod/parcela))
elif opcao == 2:
    preco_atualizado = prod * 0.95
    print('O valor total do produto será de R$ {:.2f} com Cinco porcento de desconto à vista no cartão.'.format(preco_atualizado))
elif opcao == 4:
    parcela = int(input('Informe a quantidade de parcelas que deseja realizar o pagamento: '))
    preco_atualizado = prod * 1.2
    print('O valor total do produto será R${:.2f} e será dividido em {} vezes que resultará em parcelas de R$ {:.2f}'.format(preco_atualizado, parcela, preco_atualizado / parcela))    
elif opcao == 1:
    preco_atualizado = prod * 0.9
    print('O valor total do produto será de R$ {:.2f} com Dez porcento de desconto à vista em Dinheiro/Cheque'.format(preco_atualizado))
else:
    print('Opção inválida, tente novamente.')

    