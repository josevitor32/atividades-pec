
def separar_dezena(n):
    d = (n // 10 ) % 10
    return d

def separar_unidade(n):
    u = n % 10
    return u


def par_d(d,par_):
    if d % 2 != 0:
        return par_ + 1
    else:
        return par_

def par_u(u,p_d):
    if u % 2 != 0:
        return p_d + 1
    else:
        return p_d
    
    
    


def main():
    n = int(input('Digite um número entre 10 e 99: '))

    par_ = 0

    d = separar_dezena(n)

    u = separar_unidade(n)

    p_d = par_d(d,par_)

    p_u = par_u(u,p_d)

    if p_u == 0:
        print('Nenhum dígito é ímpar.')
    elif p_u == 1:
        print('Apenas um dígito é ímpar.')
    else:
        print('Os dois dígitos são ímpares.')
        


if __name__ == '__main__':
    main()
