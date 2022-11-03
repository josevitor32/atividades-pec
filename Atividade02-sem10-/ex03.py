def musica(n,m,i):
    for k in range(n,m,i):
        if k < 251:
            print(f'{k} bugs no software, pegue um deles e conserte...')
            print('Tecle "Ctrl+F5"')


def main():
    musica(99,252,7)
    print('Vamos fazer mais um café!')
    
    

if __name__ == '__main__':
    main()
