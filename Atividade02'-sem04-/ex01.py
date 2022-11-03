n1 = input('digite um valor: ').strip()
n2 = input('digite outro valor: ').strip()
n1_float = float(n1)
n2_float = float(n2)
soma = n1_float + n2_float
concatenacao = (str(n1_float) + n2)
produto = n1_float * n2_float
produtostring = str(n1_float) * int(n2)
divisao = n1_float / n2_float
divisaointeira = n1_float // n2_float
expo = n1_float ** n2_float
resto = n1_float % n2_float
print('a soma entre {} e {} é {}'.format(n1,n2,soma))
print('a concatenação das strings é {}'.format(concatenacao))
print('a multiplicação entre {} e {} é {}'.format(n1,n2,produto))
print('a multiplicação como string é {}'.format(produtostring))
print('a divisão entre {} e {} é {}'.format(n1,n2,divisao))
print('a divisão inteira é {}'.format(divisaointeira))
print('a exponenciação entre {} e {} é {}'.format(n1,n2,expo))
print('o resto da divisão entre {} e {} é {}'.format(n1,n2,resto))





           
