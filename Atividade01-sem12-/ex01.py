def minutos(mts):
    min1 = 0
    lebre = 0
    while mts > lebre:
        min1 += 1
        lebre += 10
        mts += 1
    return(min1)
              

def main():
    metros_frente = int(input('quantos metros a tartaruga saiu a frente: '))
    
    m = minutos(metros_frente)
    
    print(f'a lebre alcançará a tartaruga em {m} minutos')

if __name__ == '__main__':
    main()
