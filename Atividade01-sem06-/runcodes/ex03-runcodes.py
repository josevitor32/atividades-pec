def horas(seg):
    return seg // 3600

def minutos(seg):
    return (seg % 3600) // 60

def segundos(seg):
    return (seg % 3600) % 60


def main():
    s = int(input())
    
    hora = horas(s)
    
    minuto = minutos(s)
    
    segundo = segundos(s)
    
    print(f'{hora}:{minuto}:{segundo}')



if __name__ == '__main__':
    main()
