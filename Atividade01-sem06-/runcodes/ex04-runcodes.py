def maior(n1, n2, n3, n4, n5):
    return max(n1, n2, n3, n4, n5)

def menor(n1, n2, n3, n4, n5):
    return min(n1, n2, n3, n4, n5)

def media(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5


def main():
    n1 = int(input())
    
    n2 = int(input())
    
    n3 = int(input())
    
    n4 = int(input())
    
    n5 = int(input())
    
    maior(n1, n2, n3, n4, n5)
    
    menor(n1, n2, n3, n4, n5)
    
    media(n1, n2, n3, n4, n5)

    
    print(f'{maior(n1, n2, n3, n4, n5)}')

    print(f'{menor(n1, n2, n3, n4, n5)}')

    print(f'{media(n1, n2, n3, n4, n5)}')



if __name__ == '__main__':
    main()
