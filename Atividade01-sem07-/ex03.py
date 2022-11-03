def sinal(s):
    if s.upper() == 'V':
        return 'Siga'
    elif s.upper() == 'A':
        return 'Atenção'
    else:
        return 'Pare'
        



def main():
    s = input('Digite a cor do sinal, "V" para verde, "A" para amarelo e "E" para vermelho: ')
    
    s1 = sinal(s)
    
    print(f'{s1}')


if __name__ == '__main__':
    main()
