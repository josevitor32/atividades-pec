def pergunta(p):
    if p.lower() == 'a':
        return 'não, texto é um tipo de dado :('
    elif p.lower() == 'b':
        return 'resposta correta!'
    elif p.lower() == 'c':
        return 'resposta errada!'
    else:
        return 'você nao digitou a opção a,b ou c :('


def main():
    p = input('''
     Q1 - No python, como se chama uma 'caixa' usada para armazenar dados?
     a) - texto
     b) - variável
     c) - uma caixa de sapatos
     ''').strip()

    p1 = pergunta(p)

    print(p1)

if __name__ == '__main__':
    main()
