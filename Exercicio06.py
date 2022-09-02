#FUA para ler dois inteiros (variáveis A e B) e efetuar as operações de adição, subtração, 
# multiplicação e divisão de A por B apresentando ao final os quatro resultados obtidos. 
A = int(input('Digite um valor: '))
B = int(input('Digite outro valor: '))
SOM= A + B 
SUB= A - B
DIV= A / B
MUL= A * B
print ('A soma entre {} e {} é igual a {}!'.format(A, B, SOM))
print ('A subtração entre {} e {} é igual a {}!'.format(A, B, SUB))
print ('A divisão entre {} e {} é igual a {}!'.format(A,B,DIV))
print ('A multiplicação entre {} e {} é igual a {}!'.format(A,B,MUL))