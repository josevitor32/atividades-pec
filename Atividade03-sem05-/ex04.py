def horas(minutos):
    return minutos // 60

def resto(minutos):
    return minutos % 60

def main():
    min = int(input('digite a quantidade de minutos: '))

    h = horas(min)

    r = resto(min)

    print(f'{min} equivalem a {h}:{r} em formato de horas.')

if __name__ == '__main__':
    main()

    
          
