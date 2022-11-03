def main():
    c = 0
    while True:
        n = int(input('Digite um número inteiro: '))
        if n != 0:
            c += n
        if n == 0:
            break
    print(f'A soma dos números é {c}')

if __name__ == '__main__':
    main()
