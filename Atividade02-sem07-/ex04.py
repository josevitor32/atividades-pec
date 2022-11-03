def signo(dia, mes):
    if mes == 12 and dia >= 22 and dia <= 31 or mes == 1  and dia >= 1  and dia <= 20:
        return 'Capricornio'
    elif mes == 1 and dia >= 21 and dia <= 31 or mes == 2 and dia >= 1  and dia <= 19:
        return 'Aquario'
    elif mes == 2 and dia >= 20 and dia <= 29 or mes == 3 and dia >= 1  and dia <= 20:
        return 'Peixes'
    elif mes == 3 and dia >= 21 and dia <= 31 or mes == 4 and dia >= 1  and dia <= 20:
        return" Aries"
    elif mes == 4 and dia >= 21 and dia <= 30 or mes == 5 and dia >= 1  and dia <= 20:
        return 'Touro'
    elif mes == 5 and dia >= 21 and dia <= 31 or mes == 6 and dia >= 1  and dia <= 20:
        return 'Gemeos'
    elif mes == 6 and dia >= 21 and dia <= 30 or mes == 7 and dia >= 1  and dia <= 21:
        return 'Cancer'
    elif mes == 7 and dia >= 22 and dia <= 31 or mes == 8 and dia >= 1  and dia <= 22:
        return 'Leao'
    elif mes == 8 and dia >= 23 and dia <= 31 or mes == 9 and dia >= 1  and dia <= 22:
        return 'Virgem'
    elif mes == 9  and dia >= 23 and dia <= 30 or mes == 10 and dia >= 1  and dia <= 22:
        return ' Libra'
    elif mes == 10 and dia >= 23 and dia <= 31 or mes == 11 and dia >= 1  and dia <= 21:
        return 'Escorpiao'
    elif mes == 11 and dia >= 22 and dia <= 30 or mes == 12 and dia >= 1  and dia <= 21:
        return 'Sagitario'
    else:
        return 'Erro: dia ou mes de nascimento invalidos !!'

def main():
    d = int(input('Digite seu dia de nascimento: '))
    
    m = int(input('Digite seu mês de nascimento: '))

    sig = signo(d, m)

    print(sig)

if __name__ == '__main__':
    main()
