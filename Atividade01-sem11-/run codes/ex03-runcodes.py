def main():
    c = 0
    maior = 0
    menor = 0
    while True:
        n = int(input())
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
    print(f'{maior}')
    
    print(f'{menor}')


if __name__ == '__main__':
    main()

