def maior(n):
    total = 0
    for k in range(n):
       numero = int(input())
       total += numero
    return total / n


def main():
    numero = maior(100);
    print(f'{numero:.2f}')


if __name__ == '__main__':
    main()
