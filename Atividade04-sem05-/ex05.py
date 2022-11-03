def vogal(letra):
    if letra == "'" or letra == '"' or letra == '!' or letra == '@' or letra == '#' or letra == '$' or letra == '%' or letra == '¨' or letra == '&' or letra == '*' or letra == '(' or letra == ')' or letra == '_' or letra == '-' or letra == '=' or letra == '+' or letra == '/' or letra == '*' or letra == '´' or letra == '`' or letra == '[' or letra == '{' or letra == '~' or letra == '^' or letra == ']' or letra == '}' or letra == ',' or letra == '.' or letra == ':' or letra == ';' or letra == '/' or letra == '?' or letra == 'Ç':
        return True
    else:
        return False
    
def main():
    letra = (input('Digite um simbolo: '))
    
    c1 = vogal(letra)
    
    print((c1))
    

if __name__ == '__main__':
    main()
    
    

