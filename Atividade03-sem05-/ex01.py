def calcular(a,b,c):
    return (2 * a) + (5 * b) - c

def main():
    a1 = int(input('digite um valor para a: '))
    b2 = int(input('digite um valor para b: '))
    c3 = int(input('digite um valor para c: '))

    
    print(f'2 X {a1} + 5 X {b2} - {c3} = {(calcular(a1, b2, c3))}')

if __name__ == '__main__':
    main()
