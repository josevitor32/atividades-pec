def sexo(s):
    if s == 1:
        return 'Ilmo Sr'
    else:
        return 'Ilma Sra'
        

def main():
    n = input('Digite seu nome: ')
    
    s = int(input('informe seu sexo, digite 1 para masculino ou 2 para feminino: '))
    
    s1 = sexo(s)
    
    print(f'{s1} {n}')


if __name__ == '__main__':
    main()
