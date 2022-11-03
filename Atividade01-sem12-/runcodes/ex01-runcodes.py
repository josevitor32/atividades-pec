def minutos(mts):
    min1 = 0
    lebre = 0
    while mts > lebre:
        min1 += 1
        lebre += 10
        mts += 1
    return(min1)
              

def main():
    metros_frente = int(input())
    
    m = minutos(metros_frente)
    
    print(m)

if __name__ == '__main__':
    main()
