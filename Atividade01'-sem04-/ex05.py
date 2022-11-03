altura = float(input('digite o valor da altura da sala: '))
comprimento = float(input('digite o valor do comprimento da sala: '))
largura = float(input('digite o valor da largura da sala: '))
areapiso = largura * comprimento
volumesala = largura * comprimento * altura
areaparede = (2 * altura * largura) + (2 * altura * comprimento)
print('a área do piso da sala é {}'.format(areapiso))
print('o volume da sala é {}'.format(volumesala))
print('a área da parede da sala é {}'.format(areaparede))
