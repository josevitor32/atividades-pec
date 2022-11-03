def data(d1,m1,a1,d2,m2,a2):
    if a1 > a2:
        return (f'{d1}/{m1}/{a1}')
    elif a1 < a2:
        return (f'{d2}/{m2}/{a2}')
    elif a1 == a2 and m1 > m2:
        return (f'{d1}/{m1}/{a1}')
    elif a1 == a2 and m1 < m2:
        return (f'{d2}/{m2}/{a2}')
    elif a1 == a2 and m1 == m2 and d1 > d2:
        return (f'{d1}/{m1}/{a1}')
    elif a1 == a2 and m1 == m2 and d1 < d2:
        return (f'{d2}/{m2}/{a2}')
    elif a1 == a2 and m1 == m2 and d1 == d2:
        return (f'{d2}/{m2}/{a2}')








def main():
    d1 = int(input())

    m1 = int(input())

    a1 = int(input())

    d2 = int(input())

    m2 = int(input())

    a2 = int(input())


    d = data(d1,m1,a1,d2,m2,a2)

    print(f'{d}')


if __name__ == '__main__':
    main()
