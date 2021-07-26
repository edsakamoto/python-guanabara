# leia o pesoa e a altura de uma pessoa, calcule seu indice de massa corporal (imc) e mostre seu status de acordo com a tabela abaixo. icm abaixo de 18,5 = abaixo do peso; entre 18,5 e 25 = peso ideal; entre 25 até 30 = sobrepeso; entre 30 até 40 = obesidade; acima de 40 = obesidade morbida

peso = float(input('Digite o seu peso em KG: '))
altura = float(input('Digite a sua altura em Metros: '))
imc = round(peso / (altura ** 2), 2)

if imc < 18.5:
    print('Abaixo do peso ideal. IMC: {:.2f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Peso ideal. IMC: {:.2f}'.format(imc))
elif 25 <= imc < 30:
    print('Sobrepeso. IMC: {:.2f}'.format(imc))
elif 30 <= imc < 40:
    print('Obesidade. IMC: {:.2f}'.format(imc))
elif imc >= 40:
    print('Obesidade morbida. IMC: {:.2f}'.format(imc))
