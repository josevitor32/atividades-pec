def horas(minutos):
    return minutos // 60

def resto(minutos):
    return minutos % 60

def main():
    min = int(input())

    h = horas(min)

    r = resto(min)

    print(f'{h}:{r}')

if __name__ == '__main__':
    main()

    
          
