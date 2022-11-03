def ordem(n1,n2,n3):   
    if n1 >= n2 and n1 >= n3 and n2 >= n3:
        return (n3,n2,n1)
    elif n1 >= n2 and n1 >= n3 and n3 >= n2:
        return n2, n3, n1
    elif n2 >= n1 and n2 >= n3 and n1 >= n3:
        return n3, n1, n2
    elif n2 >= n1 and n2 >= n3 and n3 >= n1:
        return n1, n3, n2
    elif n3 >= n1 and n3 >= n2 and n1 >= n2:
        return n2, n1, n3
    elif n3 >= n1 and n3 >= n2 and n2 >= n1:
        return n1, n2, n3
        
    


def main():
    n1 = int(input())

    n2 = int(input())

    n3 = int(input())

    o = ordem(n1,n2,n3)

    print(o)


if __name__ == '__main__':
    main()
