def media(n2,c):
    if n2 != 0:
        media = n2 / c
        return media


def main():
    c = 0
    n2 = 0
    maior = 0
    menor = 0
    while True:
        n = int(input())
        if n != 0:
            n2 += n
            c += 1
            if c == 1:
                maior = n
                menor = n
            else:
                if n > maior:
                    maior = n
                if n < menor:
                    menor = n

        if n == 0:
            break
    print(c)
    print(media(n2,c))
    print(menor)
    print(maior)

if __name__ == '__main__':
    main()

