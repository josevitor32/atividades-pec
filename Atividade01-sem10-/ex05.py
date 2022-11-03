def maior(n):
    maior = 0

    for k in range(n):
       numero = int(input('Digite um número inteiro: '))
       if numero > maior:
           maior = numero
    return maior


def main():
    numero = maior(100);
    
    print(f'O maior número é {numero}.')


if __name__ == '__main__':
    main()
