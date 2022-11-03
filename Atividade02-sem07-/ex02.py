def separar_centena(n):
    c = n // 100
    return c


def separar_dezena(n):
    d = (n // 10 ) % 10
    return d

def separar_unidade(n):
    u = n % 10
    return u


def par_c(c,par_):
    if c % 2 == 0:
        return par_ + 1
    else:
        return par_

def par_d(d,p_c):
    if d % 2 == 0:
        return p_c + 1
    else:
        return p_c

def par_u(u,p_d):
    if u % 2 == 0:
        return p_d + 1
    else:
        return p_d
    
    
    


def main():
    n = int(input('Digite um número entre 100 e 999: '))

    par_ = 0
    
    c = separar_centena(n)

    d = separar_dezena(n)

    u = separar_unidade(n)

    p_c = par_c(c,par_)

    p_d = par_d(d,p_c)

    p_u = par_u(u,p_d)
    
    print(f'O número {n} possui {p_u} dígitos pares.')

if __name__ == '__main__':
    main()
