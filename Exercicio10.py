#F.U.A que leia o preço de um produto e a quantidade comprada 
# e exiba para o usuário o preço que ele tem que pagar pela compra.
preço = int(input('Digite o preço do produto:'))
quantidade = int(input('Digite a quantidade de produtos que você comprou:'))
valor = (preço * quantidade)
print(f' O total a pagar pela sua compra será R$ {valor}')