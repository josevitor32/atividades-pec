def civil(e):
    if e == 1:
        return input().strip()
    else:
        return 0

def soma(n,e1):
    if e1 == 0:
        return len(n.replace(' ',''))
    else:
        return len(n.replace(' ','')) + len(e1.replace(' ',''))
    


def main():
    n = input().strip()
     
    e = int(input())
    e1 = civil(e)
    s = soma(n,e1)
    print(s)


if __name__ == '__main__':
    main()
