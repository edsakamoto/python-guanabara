#leia o primeiro termo e a razao de uma progressao aritmetica. no final mostre os 10 prmimeiros termos dessa progressao.
primeiro = int(input('primeiro termo: '))
razao = int(input('razao: '))
contador = 0
decimo = primeiro + (10-1) * razao
for cont in range(primeiro, decimo + razao, razao):
    contador = contador + 1
    if contador < 11:
        print(cont,end=' -> ')
print('Acabou')


