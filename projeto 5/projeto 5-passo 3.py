from random import *

tentativas = 0

score = 0


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

while score < 3:
    tentativas += 1

    print(f"\nTenativa {tentativas}: Escolha uma porta (1, 2 ou 3):")

    portaEscolhida = int(input())

    portaCerta = randint(1,3)
    
    print('A porta escolhida foi a', portaEscolhida)

    print('A porta certa é a', portaCerta)

    if portaEscolhida == portaCerta:
        print('Parabéns!')
        score += 1
    else:
        print('Que peninha!')

    print(f'A sua pontuação atual é {score}')


print(f'\n** Você conseguiu terminou o jogo em {tentativas} tentativas **')

