raio = float(input('qual o valor do raio da circunferência? '))
pi = float('3.14')
comprimento = 2 * pi * raio
areac = pi * raio**2
areae = 4 * pi**2
volumee = 4 * pi * raio**3 / 3
print('o comprimento da circunferência é: {:.6f}'.format(comprimento))
print('a área do circulo é: {:.6f}'.format(areac))
print('a área da esfera é: {:.6f}'.format(areae))
print('o volume da esfera é: {:.6f}'.format(volumee)) 
