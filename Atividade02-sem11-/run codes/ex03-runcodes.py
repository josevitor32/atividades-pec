def main():
    n = 'a'
    total = 0
    while (n != 'X'):

        n = input().strip()

        if n == 'H':
            total += 5.50

        elif n == 2:
            print('2 - Vamos estudar mais.')

        elif n == 3:
            print('3 - Meus Parabéns!')

        elif n == 0:
            print('0 - Fim de serviço.')
        else:
            print('Opção inválida.')
        

if __name__ == '__main__':
    main()
    
