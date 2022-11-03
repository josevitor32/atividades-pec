def horas(seg):
    return seg // 3600

def minutos(seg):
    return (seg % 3600) // 60

def segundos(seg):
    return (seg % 3600) % 60


def main():
    s = int(input('Digite a quantidade de segundos: '))
    
    hora = horas(s)
    
    minuto = minutos(s)
    
    segundo = segundos(s)
    
    print(f'A duração do evento é {hora}:{minuto}:{segundo}')



if __name__ == '__main__':
    main()
