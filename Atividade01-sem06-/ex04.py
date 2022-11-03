def maior(n1, n2, n3, n4, n5):
    return max(n1, n2, n3, n4, n5)

def menor(n1, n2, n3, n4, n5):
    return min(n1, n2, n3, n4, n5)

def media(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5


def main():
    n1 = int(input('Digite o primeiro número inteiro: '))
    
    n2 = int(input('Digite o segundo número inteiro: '))
    
    n3 = int(input('Digite o terceiro número inteiro: '))
    
    n4 = int(input('Digite o quarto número inteiro: '))
    
    n5 = int(input('Digite o quinto número inteiro: '))
    
    maior(n1, n2, n3, n4, n5)
    
    menor(n1, n2, n3, n4, n5)
    
    media(n1, n2, n3, n4, n5)

    
    print(f'O maior número é {maior(n1, n2, n3, n4, n5)}')

    print(f'O menor número é {menor(n1, n2, n3, n4, n5)}')

    print(f'A média dos números é {media(n1, n2, n3, n4, n5)}')



if __name__ == '__main__':
    main()
