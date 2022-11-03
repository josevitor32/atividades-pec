def percentual(valor, porcentagem):
    return valor * (porcentagem / 100)

def acrescido(valor, result):
    return valor + result

def desconto(valor, result):
    return valor - result

def main():
    valor = float(input('digite o valor do produto: '))
    
    porcentagem = int(input('digite a porcentagem: '))

    p = percentual(valor, porcentagem)

    acre = acrescido(valor, p)

    des = desconto(valor, p)

    print(f'o valor acrescido é {acre:.2f}')

    print(f'o valor com desconto é {des:.2f}')

if __name__ == '__main__':
    main()



    
