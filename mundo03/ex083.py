"""
crie um programa onde o usuario digite uma expressão qualquer que use parenteses. Seu aplicativo devera analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.

"""
p = '('
t = ')'
expressao = str(input('Digite uma expressão: ')).strip().upper()
if expressao.count(p) == expressao.count(t):    
    print(f'Sua expressão: "{expressao}" está correta')
else:
    print(f'A expressão "{expressao}" está errado (tem parenteses a mais ou a menos)')

