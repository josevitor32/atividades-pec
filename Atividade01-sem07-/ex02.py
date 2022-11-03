def par_ou_impar(n):
    return n % 2 != 0
  

def main():
    n = int(input('Digite um número: '))
    
    n1 = par_ou_impar(n)
    
    print(f'{n1}')


if __name__ == '__main__':
    main()
