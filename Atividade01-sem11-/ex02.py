def media(n2,c):
    media = n2 / c
    return media


def main():
    c = 0
    n2 = 0
    n = int(input('Digite um número inteiro positivo: '))
    while (n != 0):
        n = int(input('Digite um número inteiro positivo: '))
        n2 += n
        c += 1
    if (c != 0):
        print(f'A média dos números é {media(n2,c)}')


if __name__ == '__main__':
    main()

