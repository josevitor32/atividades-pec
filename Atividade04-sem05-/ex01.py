def vogal(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        return True
    else:
        return False
    
def main():
    letra = (input('digite uma vogal: '))
    
    letra1 = vogal(letra)
    
    print((letra1))

if __name__ == '__main__':
    main()
    
    

