#Uma loja de animais precisa de um algoritmo para calcular os custos de criação de coelhos. 
# O custo é calculado com a fórmula CUSTO=(NRO_COELHOS*0.70)/18+10. 
# O algoritmo tem como entrada o número de coelhos, devendo fornecer, como saída, o custo.
coelhos = int(input('Digite o número de coelhos:'))
s = (coelhos * 0.70) /18 + 10
print (f' O custo da criação de {coelhos} coelhos é R$ {s}')
