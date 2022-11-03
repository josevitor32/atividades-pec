def dobro(v,j):
    ano = 0
    x = v * 2
    while not v >= x:
        ano += 1
        v += ((v * j) / 100)
    return ano


def main():
    v = float(input())

    j =int(input())

    d = dobro(v,j)

    print(f'{d}')

if __name__ == '__main__':
    main()

