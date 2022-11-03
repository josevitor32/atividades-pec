def percentual(valor, porcentagem):
    return valor * (porcentagem / 100)

def acrescido(valor, result):
    return valor + result

def desconto(valor, result):
    return valor - result

def main():
    valor = float(input())
    
    porcentagem = float(input())

    p = percentual(valor, porcentagem)

    acre = acrescido(valor, p)

    des = desconto(valor, p)

    print(f'{acre:.2f}')

    print(f'{des:.2f}')

if __name__ == '__main__':
    main()



    
