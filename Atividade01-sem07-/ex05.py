def nota(n1, n2, n3):
    if n3 > 8:
        return (n1 + n2 + (n3 + 1)) / 3
    else:
        return (n1 + n2 + n3) / 3


def main():
    n1 = int(input('Digite a primeira nota: '))
    
    n2 = int(input('Digite a segunda nota: '))
    
    n3 = int(input('Digite a terceira nota: '))
    
    nt = nota(n1, n2, n3)

    if nt <= 10:
        print(f'{nt:.2f}')
    else:
        print(10.00)

    

if __name__ == '__main__':
    main()


    
