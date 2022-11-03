def nota(n1, n2, n3):
    if n3 > 8:
        return ((n1 + n2 + n3 ) / 3) + 1
    else:
        return (n1 + n2 + n3) / 3


def main():
    n1 = int(input())
    
    n2 = int(input())
    
    n3 = int(input())
    
    nt = nota(n1, n2, n3)

    if nt <= 10:
        print(f'{nt:.2f}')
    else:
        print(10.00)

    

if __name__ == '__main__':
    main()


    
