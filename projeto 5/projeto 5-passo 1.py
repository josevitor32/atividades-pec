from random import *
print('''
porta da fortuna!
==========

Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!

 ____       ____    ____
|    |     |    |  |    |
| [1]|     | [2]|  | [3]|
|   o|     |   o|  |   o|
|____|     |____|  |____|

''')

for attempt in range(3):
    print('\nEscolha uma portam 1,2 ou 3):')

    portaEscolhida = int(input())

    portaCerta = randint(1,3)

    print('A porta escolhida foi a', portaEscolhida)

    print('A porta certa é a', portaCerta)

    if portaEscolhida == portaCerta:
        print('Parabéns!')
    else:
        print('Que peninha!')
