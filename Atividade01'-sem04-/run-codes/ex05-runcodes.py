altura = float(input())
comprimento = float(input())
largura = float(input())
areapiso = largura * comprimento
volumesala = largura * comprimento * altura
areaparede = (2 * altura * largura) + (2 * altura * comprimento)
print('{}'.format(areapiso))
print('{}'.format(volumesala))
print('{}'.format(areaparede))
