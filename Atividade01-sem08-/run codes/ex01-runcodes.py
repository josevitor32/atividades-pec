def idade(d,m,a,da,ma,aa):
    if ma < m:
        return (aa - a) - 1
    elif ma == m and da < d:
        return (aa - a) - 1
    else:
        return aa - a


def main():
    da = int(input())

    ma = int(input())

    aa = int(input())

    d = int(input())

    m = int(input())

    a = int(input())


    i = idade(d,m,a,da,ma,aa)

    print(f'{i}')


if __name__ == '__main__':
    main()
