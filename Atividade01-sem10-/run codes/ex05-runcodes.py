def maior(n):
    maior = 0

    for k in range(n):
       numero = int(input())
       if numero > maior:
           maior = numero
    return maior


def main():
    numero = maior(100);
    print(f'{numero}')


if __name__ == '__main__':
    main()
