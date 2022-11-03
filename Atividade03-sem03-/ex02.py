preço = float(input('qual o valor do produto? R$'))
desconto = (preço * 10) / 100
novo = preço - desconto
print('o produto custava R${:.2f}, com 10% de desconto custa R${:.2f}'.format(preço,novo))
                    
