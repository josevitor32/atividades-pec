def numero(n):
    par = 0
    impar = 0
    for k in range(n):
       numero = int(input('Digite um número inteiro: '))
       if numero % 2 == 0:
           par += 1
       else:
           impar += 1
    return par


def main():
    par_impar = numero(100);
    
    print(f'{par_impar} números são pares.')
    
    print(f'{100 - par_impar} números são impares.')


if __name__ == '__main__':
    main()
