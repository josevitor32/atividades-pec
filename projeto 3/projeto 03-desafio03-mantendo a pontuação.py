def pergunta1(p,score):
    if p.lower() == 'b':
        return score + 1
    
    else:
        return score

def pergunta2(p2,pe2):
    if p2.lower() == 'c':
        return pe2 + 1
    
    else:
        return pe2

def pergunta3(p3,pe3):
    if p3.lower() == 'a':
        return pe3 + 1
    
    else:
        return pe3



def main():
    print('Para cada resposta correta você ganhará um ponto no seu score!')
    score = 0
    p = input('''
     Q1 - No python, o símbolo "/" é usado para?
     a) - soma
     b) - divisão
     c) - subtração
     ''').strip()

    
    p2 = input('''
     Q1 - No python, o símbolo "*" é usado para?
     a) - soma
     b) - divisão
     c) - multiplicação
     ''').strip()

    p3 = input('''
     Q1 - No python, o símbolo "-" é usado para?
     a) - subtração
     b) - divisão
     c) - soma
     ''').strip()

    p1 = pergunta1(p,score)
    
    pe2 = pergunta2(p2,p1)

    pe3 = pergunta3(p3,pe2)

    print(f'Seu score total foi {pe3}')

if __name__ == '__main__':
    main()
