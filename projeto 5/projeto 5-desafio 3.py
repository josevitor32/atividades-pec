from random import *

jogando = True

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

while jogando == True:

    print("\nEscolha uma porta (1, 2 ou 3):")

    portaEscolhida = int(input())

    portaCerta = randint(1,3)
    
    print('A porta escolhida foi a', portaEscolhida)

    print('A porta certa é a', portaCerta)

    if portaEscolhida == portaCerta:
        print('Parabéns!')
        score += 1
    else:
        print('Que peninha!')
        score = 0

    print(f'A sua pontuação é {score}')

    print("\nVocê quer jogar de novo? (s/n)")
    resposta = input().lower()

    if resposta == 'n' or resposta == 'nao' or resposta == 'não':
        jogando = False

print('Obrigado por jogar.')
print(f'A sua pontuação final é {score}')

