def alfabeto(letra):
    if letra == 'a' or letra == 'b' or letra == 'c' or letra == 'd' or letra == 'e' or letra == 'f' or letra == 'g' or letra == 'h' or letra == 'i' or letra == 'j' or letra == 'k' or letra == 'l' or letra == 'm' or letra == 'n' or letra == 'o' or letra == 'p' or letra == 'q' or letra == 'r' or letra == 's' or letra == 't' or letra == 'u' or letra == 'v' or letra == 'w' or letra == 'x' or letra == 'y' or letra == 'z' or letra == 'A' or letra == 'B' or letra == 'C' or letra == 'D' or letra == 'E' or letra == 'F' or letra == 'G' or letra == 'H' or letra == 'I' or letra == 'J' or letra == 'K' or letra == 'L' or letra == 'M' or letra == 'N' or letra == 'O' or letra == 'P' or letra == 'Q' or letra == 'R' or letra == 'S' or letra == 'T' or letra == 'U' or letra == 'V' or letra == 'W' or letra == 'X' or letra == 'Y' or letra == 'Z':
        return True
    else:
        return False

def main():
    letra = input()
    
    letra1 = alfabeto(letra)
    
    print(bool(letra1))

if __name__ == '__main__':
    main()
    
