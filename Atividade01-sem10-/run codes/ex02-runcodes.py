def numero(n):
    par = 0
    impar = 0
    for k in range(n):
       numero = int(input())
       if numero % 2 == 0:
           par += 1
       else:
           impar += 1
    return par


def main():
    par_impar = numero(100);
    print(par_impar)
    print(100 - par_impar)


if __name__ == '__main__':
    main()
