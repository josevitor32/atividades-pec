def sexo(s):
    if s == 1:
        return 'Ilmo Sr.'
    else:
        return 'Ilma Sra.'
        

def main():
    n = input().strip()
    s = int(input())
    s1 = sexo(s)
    print(f'{s1} {n}')


if __name__ == '__main__':
    main()
