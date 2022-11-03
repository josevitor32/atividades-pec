def musica(n,m):
    for k in range(n,m):
        if k < 250:
            print(f'{k} bugs no software, pegue um deles e conserte...')
            print('Tecle “Ctrl+F5”')
        else:
            print('Vamos fazer mais um café!')


def main():
    musica(99,251)
    
    

if __name__ == '__main__':
    main()
