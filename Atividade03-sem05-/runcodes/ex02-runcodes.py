def perimetro(per):
    return per * 4
def area(la):
    return la * la
def main():
    l1 = float(input())

    print(f'{area(l1):>10.4f}')

    print(f'{perimetro(l1):>10.4f}')

if __name__ == '__main__':
    main()

