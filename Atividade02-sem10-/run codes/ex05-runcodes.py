def valor(n,m):
    v = float(input())
    
    for k in range(n,m):

            p = v / k
            
            print(f'{k}x de R$ {p:.2f}')


def main():
    valor(1,25)
    
    

if __name__ == '__main__':
    main()
