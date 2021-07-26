#programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posicao ela aparece a primeira vez e em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('A frase digitada: {}'.format(frase))
print('Qntidade de "A" que contem na frase: {}'.format(frase.count('A')))
print('Em qual posição ela aparece pela primeira vez: {}'.format(frase.find('A') + 1))
print('Em qual posição ela aparece pela ultima vez vez: {}'.format(frase.rfind('A') + 1))

