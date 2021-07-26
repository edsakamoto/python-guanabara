#programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome

nome = str(input('Digite o seu nome completo: ')).upper().strip()
#quebrando_nome = nome.split()
#print(nome.find('SILVA'))
print('O nome digitado possui SILVA? {}'.format(nome.find('SILVA') != -1))
#print(nome.find('SILVA') != -1)
