def main():
    n = "a"
    while (n != 0):

        n = float(input('Digite a sua nota: '))

        if 8.5 <= n <= 10:
            print('A')

        elif 7.0<= n < 8.5:
            print('B')

        elif n >= 5.0 and n < 7.0:
            print('C')

        elif n >= 4 and n < 5.0:
            print('D')
        elif n >= 0 and n < 4.0:
            print('E')
        else:
            print('Nota inválida.')

if __name__ == '__main__':
    main()
    
