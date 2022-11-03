def tempo(A,B):
    t = 0
    while A > B:
        t += 1
        A += (2 * A) / 100
        B += (3 * B) / 100

    return(t)

def tempo2(A,B):
    t = 0
    while B > A:
        t += 1
        A += (3 * A) / 100
        B += (2 * B) / 100

    return(t)
              
              

def main():
    A = int(input())
    
    B = int(input())

    if A > B:
        t = tempo(A,B)
    elif B > A:
        t = tempo2(A,B)
     
    
    print(f'{t}')

if __name__ == '__main__':
    main()
