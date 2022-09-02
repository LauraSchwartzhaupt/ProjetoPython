#Faça um algoritmo (FUA) que lê o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. O algoritmo deve calcular e mostrar o salário deste funcionário

N = input ("Qual é o seu nome?")
H = float(input("Quantas horas você trabalha semanalmente?"))
V = float(input("Qual é o valor que você recebe por hora trabalhada?"))
S = float(H*V)*4
print (" Você {} recebe um salário de: {}!".format(N,S))
