#o mesmo professor do desafio 19 quer sortear a ordem de apresentacao de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
a1 = str(input("Digite o nome do primeiro aluno: "))
a2 = str(input("Digite o nome do segundo aluno: "))
a3 = str(input("Digite o nome do terceiro aluno: "))
a4 = str(input("Digite o nome do quarto aluno: "))
lista = [a1,a2,a3,a4]
#escolhido = shuffle(lista)
shuffle(lista)
#print("O aluno sorteado é o: {}".format(escolhido))
print("A sequencia das apresentações será: {}".format(lista))
