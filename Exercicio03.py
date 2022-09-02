#Faça um algoritmo que leia um número inteiro e imprima seu antecessor e seu sucessor.
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))
s = n1 + n2
antecessor = s - 1
sucessor = s + 1
print ('A soma é igual a {}!' .format(s))
print ('O valor do antecessor é:' + repr (antecessor))
print ('O valor do sucessor é:' + repr (sucessor))