def main():
    c = 0
    while True:
        n = int(input())
        if n != 0:
            c += n
        if n == 0:
            break
    print(c)

if __name__ == '__main__':
    main()
