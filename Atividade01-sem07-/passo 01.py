def resposta(r):
    if r == 'variavel':
        return ':)' * 100
    


def main():
    r = input('No python, como se chama uma "caixa" usada para armazenar dados? ')
    
    r1 = resposta(r)
    
    print(f'{r1}')

    print('Obrigado por jogar!')

if __name__ == '__main__':
    main()
    
