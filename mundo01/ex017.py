#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um trinagulo retangulo. Calcucule e mostre o comprimento da hipotenusa
import math
a = float(input("Digite o valor de um dos catetos: "))
b = float(input("digite o valor do cateto oposto: "))
c = (a ** 2 + b ** 2) ** 0.5
print("O valor da hipotenusa é: ",c)
print("o valor da hipotenusa utilizando função hypot da biblioteca math: ", math.hypot(a,b))

