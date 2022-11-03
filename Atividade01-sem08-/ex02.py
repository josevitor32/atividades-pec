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
    print('Digite duas datas diferentes.')

    d1 = int(input('Digite o dia da primeira data: '))

    m1 = int(input('Digite o mês da primeira data: '))

    a1 = int(input('Digite o ano da primeira data: '))

    d2 = int(input('Digite o dia da segunda data: '))

    m2 = int(input('Digite o mês da segunda data: '))

    a2 = int(input('Digite o ano da segunda data: '))

    d = data(d1,m1,a1,d2,m2,a2)

    print(f'A data mais recente é {d}')


if __name__ == '__main__':
    main()
