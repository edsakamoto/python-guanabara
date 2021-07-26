# refaça o ex 09, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laço FOR

tab = int(input('Digita o número da tabuada que deseja visualizar: '))
for c in range(0,11):    
    print('{} x {} = {}'.format(tab, c, tab * c))
