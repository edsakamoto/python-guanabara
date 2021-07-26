""" 
simular um funcionamento de um caixa eletronico. No inicio pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues.
obs:
só há cedulas de R$50, 20, 10, 1

"""

c_50 = c_20 = c_10 = c_01 = 0
total = 0
sobra = 0
while True:
    x = int(input('Digite o valor do saque: R$ '))
    total = x    
    if x < 0:
        print('Valor digitado inválido, tente novamente')
        break
    elif x > 0:
        if divmod(x,50)[0] > 0:
            c_50 = divmod(x,50)[0]
            total = total - (divmod(x,50)[0] * 50)
            sobra = divmod(x,50)[1]
            if divmod(sobra,20)[0] > 0 and total > 0:
                c_20 = divmod(sobra,20)[0]
                total = total - (divmod(sobra,20)[0] * 20)
                sobra = divmod(sobra,20)[1]
                if divmod(sobra,10)[0] > 0 and total > 0:
                    c_10  = divmod(sobra,10)[0]
                    total = total - (divmod(sobra,10)[0] * 10)
                    c_01  = divmod(sobra,10)[1]
                else:
                    c_01  = divmod(sobra,10)[1] 
                    break
            else: 
                c_01 = divmod(sobra,20)[1]
                break
        elif divmod(x,20)[0] > 0:
            c_20 = divmod(x,20)[0]
            total = total - (divmod(x,20)[0] * 20)
            sobra = divmod(x,20)[1]
            if divmod(sobra,10)[0] > 0 and total > 0:
                c_10  = divmod(sobra,10)[0]
                total = total - (divmod(sobra,10)[0] * 10)
                c_01  = divmod(sobra,10)[1]
                break
            else: 
                c_01  = divmod(sobra,10)[1]
                break
        elif divmod(x,10)[0] > 0:
            c_10 = divmod(x,10)[0]
            total = total - (divmod(x,10)[0] * 10)
            c_01 = divmod(x,10)[1]
            break
        else:
            c_01 = divmod(x,1)[0]
            total = total - (divmod(x,1)[0] * 1)
            break
print(f"""
--------------------------------
Saque de {c_50} nota(s) de 50 R$
Saque de {c_20} nota(s) de 20 R$
Saque de {c_10} nota(s) de 10 R$
Saque de {c_01} nota(s) de 01 R$
Totalizando {x} reais 
--------------------------------

""")            
                
                

        
        



