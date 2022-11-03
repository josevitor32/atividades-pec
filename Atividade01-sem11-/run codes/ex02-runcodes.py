def media(n2,c):
    media = n2 / c
    return media

def main():
    c = 0
    n2 = 0
    n = int(input())
    while (n != 0):
        n2 += n
        n = int(input())
        c += 1
    if (c != 0):
        print(media(n2,c))


if __name__ == '__main__':
    main()

