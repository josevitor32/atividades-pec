def main():
    n = 8
    while (n != 0):
        print('''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')

        n = int(input('Digite a opção desejada: '))

        if n == 1:
            print('1 - Olá. Como vai?')

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
    
