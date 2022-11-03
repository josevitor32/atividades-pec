def pergunta(p):
    if p.lower() == 'variável':
        return ':)' * 100
    else:
        return ':(' * 100


def main():
    p = input("No python, como se chama uma 'caixa' usada para armazenar dados? ").strip()

    p1 = pergunta(p)

    print(p1)

    print('Obrigado por jogar!')

if __name__ == '__main__':
    main()
