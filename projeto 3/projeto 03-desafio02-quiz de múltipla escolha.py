def pergunta(p):
    if p.lower() == 'a':
        return 'resposta incorreta :('
    elif p.lower() == 'b':
        return 'resposta correta!'
    elif p.lower() == 'c':
        return 'resposta errada!'
    else:
        return 'você nao digitou a opção a,b ou c :('


def main():
    p = input('''
     Q1 - No python, o símbolo "/" é usado para?
     a) - soma
     b) - divisão
     c) - subtração
     ''').strip()

    p1 = pergunta(p)

    print(p1)

if __name__ == '__main__':
    main()
