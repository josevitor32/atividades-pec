from random import *

jogando = True

novo_numero = 0

total = 0

print('''
Vinte e um!
==========

Tente fazer extamente 21 pontos

''')

while jogando == True:

    novo_numero = randint(1,10)
    
    print('Seu próximo número é', novo_numero)

    total += novo_numero 

    print('A sua pontuação agora é', (total))

    print("\nGostaria de somar mais um número? (s/n)")
    reposta = input()

    if reposta == 'n':
        jogando = False

if total == 21:
    print('Parabéns!')

if total != 21:
    print('Que pena!')


