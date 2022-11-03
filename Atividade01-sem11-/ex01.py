def dobro(v,j):
    ano = 0
    x = v * 2
    while not v >= x:
        ano += 1
        v += ((v * j) / 100)
    return ano


def main():
    v = float(input('Digite o valor do depósito inicial: '))

    j =int(input('Digite a taxa de juros ao ano: '))

    d = dobro(v,j)

    print(f'R${v} rendendo {j}% ao ano irá dobrar em {d} anos.')

if __name__ == '__main__':
    main()

