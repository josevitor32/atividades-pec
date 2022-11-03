def caractere(c):
    if c.upper() in 'AEIOU':
        return 'vogal'
    elif c.upper() in 'BCDFGHJKLMNPQRSTVWXYZ':
        return 'consoante'
    elif c.upper() in '0987654321':
        return 'número'
    else:
        return 'símbolo'

def main():
    c = input().strip()
    c1 = caractere(c)
    print(f'{c1}')

if __name__ == '__main__':
    main()
