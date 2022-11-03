def main():
    b = 0
    n = 'a'
    while n != 'X':
        print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
        n = input('Digite o código do item comprado: ').upper()[0]
        if n == 'H':
            b += 5.50
        if n == 'M':
            b += 4.50
        if n == 'A':
            b += 7.00
        if n == 'C':
            b += 6.80
        if n == 'Q':
            b += 4.00
        if n == 'X':
            print(f'O total da compra è R${b:.2f}')

if __name__ == '__main__':
    main()


