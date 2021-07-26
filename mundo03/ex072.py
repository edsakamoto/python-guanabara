# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


while True:
    opcao = int(input('Digite um número de 0 a 20: '))
    if 0 <= opcao <= 20:
        print(f'O número digitado foi {num[opcao]}')
        continua = str(input('Você quer continuar[S/N] ? ')).strip().upper()
        if continua == 'N':
            break
    else:
        print('Opção inválida, tente novamente.')    

