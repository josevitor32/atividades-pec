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
        n = int(input('Digite uma idade: '))
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
    print(f'O número de pessoas é {c}')
    print(f'A média das idades é {media(n2,c):.2f}')
    print(f'A menor idade é {menor}')
    print(f'A maior idade é {maior}')

if __name__ == '__main__':
    main()

