def media(n1,n2,n3,n4,n5):
    return (n1 + n2 + n3 + n4 + n5) / 5


def maior(n1,n2,n3,n4,n5):
    me = (n1 + n2 + n3 + n4 + n5) / 5
    if n1 > me and n2 <= me and n3 <= me and n4 <= me and n5 <= me:
        return n1
    elif n2 > me and n1 <= me and n3 <= me and n4 <= me and n5 <= me:
        return n2
    elif n3 > me and n1 <= me and n2 <= me and n4 <= me and n5 <= me:
        return n3
    elif n4 > me and n1 <= me and n2 <= me and n3 <= me and n5 <= me:
        return n4
    elif n5 > me and n1 <= me and n3 <= me and n4 <= me and n2 <= me:
        return n5
    elif n1 > me and n2 > me and n3 <= me and n4 <= me and n5 <= me:
        return n1,n2
    elif n1 > me and n2 <= me and n3 > me and n4 <= me and n5 <= me:
        return n1,n3
    elif n1 > me and n2 <= me and n3 <= me and n4 > me and n5 <= me:
        return n1,n4
    elif n1 > me and n2 <= me and n3 <= me and n4 <= me and n5 > me:
        return n1,n5
    elif n1 > me and n2 > me and n3 > me and n4 <= me and n5 <= me:
        return n1,n2,n3
    elif n1 > me and n2 > me and n3 <= me and n4 > me and n5 <= me:
        return n1,n2,n4
    elif n1 > me and n2 > me and n3 <= me and n4 <= me and n5 > me:
        return n1,n2,n5
    elif n1 > me and n2 <= me and n3 <= me and n4 > me and n5 <= me:
        return n1,n3,n4
    elif n1 > me and n2 <= me and n3 <= me and n4 <= me and n5 > me:
        return n1,n3,n5
    elif n1 > me and n2 <= me and n3 <= me and n4 > me and n5 > me:
        return n1,n4,n5
    elif n1 <= me and n2 > me and n3 > me and n4 <= me and n5 <= me:
        return n2,n3
    elif n1 <= me and n2 > me and n3 <= me and n4 > me and n5 <= me:
        return n2,n4
    elif n1 <= me and n2 > me and n3 <= me and n4 <= me and n5 > me:
        return n2,n5
    elif n1 <= me and n2 > me and n3 > me and n4 > me and n5 <= me:
        return n2,n3,n4
    elif n1 <= me and n2 > me and n3 > me and n4 <= me and n5 > me:
        return n2,n3,n5
    elif n1 <= me and n2 > me and n3 <= me and n4 > me and n5 > me:
        return n2,n4,n5
    elif n1 <= me and n2 <= me and n3 > me and n4 > me and n5 <= me:
        return n3,n4
    elif n1 <= me and n2 <= me and n3 > me and n4 <= me and n5 > me:
        return n3,n5
    elif n1 <= me and n2 <= me and n3 > me and n4 > me and n5 > me:
        return n3,n4,n5
    elif n1 <= me and n2 <= me and n3 <= me and n4 > me and n5 > me:
        return n4,n5

    else:
        return "Você não digitou números válidos"




def main():
    n1 = int(input('Digite um número inteiro: '))

    n2 = int(input('Digite um número inteiro: '))

    n3 = int(input('Digite um número inteiro: '))

    n4 = int(input('Digite um número inteiro: '))

    n5 = int(input('Digite um número inteiro: '))

    me = media(n1,n2,n3,n4,n5)

    ma = maior(n1,n2,n3,n4,n5)


    print(f'A média é {me:.2f}')
    print(f'{ma}')


if __name__ == '__main__':
    main()

