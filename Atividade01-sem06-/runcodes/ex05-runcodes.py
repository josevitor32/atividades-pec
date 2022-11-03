def desconto(d):
    return d - ((d * 9) / 100)

def prestacao5(p):
    return p / 5

def prestacao10(p):
    return (p + ((p * 17) / 100)) / 10
    

def main():
    c = float(input())
    
    desc = desconto(c)
    
    p5 = prestacao5(c)
    
    p10 = prestacao10(c)

    print(f'{desc:.2f}')
    
    print(f'{p5:.2f}')

    print(f'{p10:.2f}')
    

if __name__ == '__main__':
    main()
              
