def pergunta(p):
    if p.lower() == 'arya':
        return 'Resposta correta!'
    elif p.lower() == 'arya stark':
        return 'Resposta correta!'
    else:
        return 'Resposta errada, o inverno está chegando!'


def main():
    p = input('Em game of thrones quem matou o rei da noite? ').strip()
    
    p1 = pergunta(p)
    
    print(p1)


if __name__ == '__main__':
    main()
