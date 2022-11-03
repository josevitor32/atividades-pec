def inverso(numero):
    return (numero[::-1])

def main():
    numero = str(input('digite um número entre 1000 e 9999: '))
    
    inver = inverso(numero)

    print(f'o inverso de {numero} é {inver}.')

if __name__ == '__main__':
    main()
    
