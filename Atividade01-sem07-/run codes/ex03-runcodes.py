def sinal(s):
    if s.upper() == 'V':
        return 'Siga'
    elif s.upper() == 'A':
        return 'Atenção'
    else:
        return 'Pare'
        



def main():
    s = input().strip()
    s1 = sinal(s)
    print(f'{s1}')


if __name__ == '__main__':
    main()
