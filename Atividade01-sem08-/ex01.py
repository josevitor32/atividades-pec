def idade(d,m,a,da,ma,aa):
    if ma < m:
        return (aa - a) - 1
    elif ma == m and da < d:
        return (aa - a) - 1
    else:
        return aa - a




def main():
    da = int(input('Digite o dia de hoje: '))

    ma = int(input('Digite o mês de hoje: '))

    aa = int(input('Digite o ano de hoje: '))

    d = int(input('Digite seu dia de nascimento: '))

    m = int(input('Digite seu mês de nascimento: '))

    a = int(input('Digite seu ano de nascimento: '))


    i = idade(d,m,a,da,ma,aa)

    print(f'A sua idade é {i}')


if __name__ == '__main__':
    main()
