def numeros(n):
    for i in range(10,n,10):
        if i != 1000:
            print(i,end=', ')
        else:
            print(i,end='.')


def main():
    numeros(1010)


if __name__ == '__main__':
    main()
