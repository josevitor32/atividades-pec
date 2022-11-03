def ordem(n1,n2,n3):   
    if n1 >= n2 and n1 >= n3 and n2 >= n3:
        return n3, n2, n1
    elif n1 >= n2 and n1 >= n3 and n3 >= n2:
        return n2, n3, n1
    elif n2 >= n1 and n2 >= n3 and n1 >= n3:
        return n3, n1, n2
    elif n2 >= n1 and n2 >= n3 and n3 >= n1:
        return n1, n3, n2
    elif n3 >= n1 and n3 >= n2 and n1 >= n2:
        return n2, n1, n3
    elif n3 >= n1 and n3 >= n2 and n2 >= n1:
        return n1, n2, n3
        
    


def main():
    n1 = int(input('Digite o primeiro número: '))

    n2 = int(input('Digite o segundo número: '))

    n3 = int(input('Digite o terceiro número: '))

    o = ordem(n1,n2,n3)

    print(o)


if __name__ == '__main__':
    main()
