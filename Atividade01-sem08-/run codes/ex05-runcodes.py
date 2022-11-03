def imc(a,p):
    return p // (a ** 2)


def msg(i):
    if i < 18.5:
        return 'Abaixo do peso'
    elif i < 25:
        return 'Peso normal'
    elif i < 30:
        return 'Sobrepeso'
    elif i < 35:
        return 'Obeso leve'
    elif i < 40:
        return 'Obeso moderado'
    elif i >= 40:
        return 'Obeso mórbido'




def main():
    p = float(input())
    
    a = float(input())

    i = imc(a,p)

    m = msg(i)

    print(f'{i:.2f}')

    print(m)


if __name__ == '__main__':
    main()
