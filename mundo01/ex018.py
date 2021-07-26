#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
angulo = float(input("digite o valor de um ângulo qualquer: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O angulo de {} tem o Seno: {:.2f} , Cosseno: {:.2f} , Tangente: {:.2f} ".format(angulo,seno,cosseno,tangente))
