#leia um numero de 0 a 9999 e mostra na tela cada um dos digitos separados
x = int(input("digite um numero entre 0 a 9999: "))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print('analisando numero {}'.format(x))
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))
