def main():
    c = 0
    maior = 0
    menor = 0
    while True:
        n = int(input('Digite um número inteiro positivo: '))
        if n != 0:
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
    print(f'O maior número é {maior}')
    print(f'O menor número é {menor}')


if __name__ == '__main__':
    main()

