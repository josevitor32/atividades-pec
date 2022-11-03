def meses(carro):
    p = 10000
    m = 0
    while carro > p:
        m += 1
        p += (0.7 * p) / 100
        carro += (0.4 * carro) / 100
    return(m)
              

def main():
    carro = float(input())
    
    m = meses(carro)
    
    print(f'{m}')

if __name__ == '__main__':
    main()
