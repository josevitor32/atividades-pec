def inverso(numero):
    return (numero[::-1])

def main():
    numero = str(input()).strip()
    
    inver = inverso(numero)

    print(f'{inver}')

if __name__ == '__main__':
    main()
    
