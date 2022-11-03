def dividaa(salario,divida):
    m = 10
    ano = 2016
    while salario > divida:
        if m != 3 or m <= 12:
            m += 1
            divida += (15 * divida) / 100
        if m == 3:
            m += 1
            salario += (5 * salario) / 100
        if m == 13:
            m = 1
            divida += (15 * divida) / 100
            ano += 1      

        if divida > salario:
            print(f'{m}/{ano}')

def main():
    salario = float(input())
    
    divida = float(input())
    
    dividaa(salario,divida)
    
    

if __name__ == '__main__':
    main()
        
    
    
