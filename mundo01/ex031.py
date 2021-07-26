#desenvolva um programa que pergunte a distancia de uma viagem em km. calcule o preço de passagem cobrando r$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = float(input('Qual será a distância da viagem? '))
if distancia <= 200:
    #print('Preço da passagem será: R${:.2f}'.format(distancia * 0.50))
    preco = distancia * 0.50
else:
    #print('Preço da passagem será: R${:.2f}'.format(distancia * 0.45))
     preco = distancia * 0.45
print('Preço da passagem será: R${:.2f}'.format(preco))