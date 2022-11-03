def caractere(carac):
    return len(carac)


def main():
    nome = input('Digite um nome: ')
    
    n = caractere(nome)
    
    print(f'{nome} possui {n} caracteres.')


if __name__ == '__main__':
    main()
