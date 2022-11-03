def maior(n):
    total = 0
    for k in range(n):
       numero = int(input('Digite um número inteiro: '))
       total += numero
    return total / n


def main():
    numero = maior(100);
    
    print(f'A média desses números é {numero:.2f}.')


if __name__ == '__main__':
    main()
