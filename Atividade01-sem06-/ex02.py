def caractere(carac):
    return ord(carac)


def main():
    c = input('Digite um caractere: ')
    
    c1 = caractere(c)
    
    print(f'o código Unicode do caractere {c} é {c1}')



if __name__ == '__main__':
    main()
