def media(n1,n2,n3,n4,n5):
    return (n1 + n2 + n3 + n4 + n5) / 5


def maior(n1,n2,n3,n4,n5):
    me = (n1 + n2 + n3 + n4 + n5) / 5
    if n1 > me and n2 <= me and n3 <= me and n4 <= me and n5 <= me:
        return (f'{n1:.2f}')
    elif n2 > me and n1 <= me and n3 <= me and n4 <= me and n5 <= me:
        return (f'{n2:.2f}')
    elif n3 > me and n1 <= me and n2 <= me and n4 <= me and n5 <= me:
        return (f'{n3:.2f}')
    elif n4 > me and n1 <= me and n2 <= me and n3 <= me and n5 <= me:
        return (f'{n4:.2f}')
    elif n5 > me and n1 <= me and n3 <= me and n4 <= me and n2 <= me:
        return (f'{n5:.2f}')
    elif n1 > me and n2 > me and n3 <= me and n4 <= me and n5 <= me:
        return (f'''{n1:.2f}
{n2:.2f}''')
    elif n1 > me and n2 <= me and n3 > me and n4 <= me and n5 <= me:
        return (f'''{n1:.2f}
{n3:.2f}''')
    elif n1 > me and n2 <= me and n3 <= me and n4 > me and n5 <= me:
        return (f'''{n1:.2f}
{n4:.2f}''')
    elif n1 > me and n2 <= me and n3 <= me and n4 <= me and n5 > me:
        return (f'''{n1:.2f}
{n5:.2f}''')
    elif n1 > me and n2 > me and n3 > me and n4 <= me and n5 <= me:
        return (f'''{n1:.2f}
{n2:.2f}
{n3:.2f}''')
    elif n1 > me and n2 > me and n3 <= me and n4 > me and n5 <= me:
        return (f'''{n1:.2f}
{n2:.2f}
{n4:.2f}''')
    elif n1 > me and n2 > me and n3 <= me and n4 <= me and n5 > me:
        return (f'''{n1:.2f}
{n2:.2f}
{n5:.2f}''')
    elif n1 > me and n2 <= me and n3 <= me and n4 > me and n5 <= me:
        return (f'''{n1:.2f}
{n3:.2f}
{n4:.2f}''')
    elif n1 > me and n2 <= me and n3 <= me and n4 <= me and n5 > me:
        return (f'''{n1:.2f}
{n3:.2f}
{n5:.2f}''')
    elif n1 > me and n2 <= me and n3 <= me and n4 > me and n5 > me:
        return (f'''{n1:.2f}
{n4:.2f}
{n5:.2f}''')
    elif n1 <= me and n2 > me and n3 > me and n4 <= me and n5 <= me:
        return (f'''{n2:.2f}
{n3:.2f}''')
    elif n1 <= me and n2 > me and n3 <= me and n4 > me and n5 <= me:
        return (f'''{n2:.2f}
{n4:.2f}''')
    elif n1 <= me and n2 > me and n3 <= me and n4 <= me and n5 > me:
        return (f'''{n2:.2f}
{n5:.2f}''')
    elif n1 <= me and n2 > me and n3 > me and n4 > me and n5 <= me:
        return (f'''{n2:.2f}
{n3:.2f}
{n4:.2f}''')
    elif n1 <= me and n2 > me and n3 > me and n4 <= me and n5 > me:
        return (f'''{n2:.2f}
{n3:.2f}
{n5:.2f}''')
    elif n1 <= me and n2 > me and n3 <= me and n4 > me and n5 > me:
        return (f'''{n2:.2f}
{n4:.2f}
{n5:.2f}''')
    elif n1 <= me and n2 <= me and n3 > me and n4 > me and n5 <= me:
        return (f'''{n3:.2f}
{n4:.2f}''')
    elif n1 <= me and n2 <= me and n3 > me and n4 <= me and n5 > me:
        return (f'''{n3:.2f}
{n5:.2f}''')
    elif n1 <= me and n2 <= me and n3 > me and n4 > me and n5 > me:
        return (f'''{n3:.2f}
{n4:.2f}
{n5:.2f}''')
    elif n1 <= me and n2 <= me and n3 <= me and n4 > me and n5 > me:
        return (f'''{n4:.2f}
{n5:.2f}''')
    elif n1 > me and n2 > me and n3 > me and n4 > me and n5 <= me:
        return (f'''{n1:.2f}
{n2:.2f}
{n3:.2f}
{n4:.2f}''')
    elif n1 > me and n2 > me and n3 > me and n4 <= me and n5 > me:
        return (f'''{n1:.2f}
{n2:.2f}
{n3:.2f}
{n5:.2f}''')
    elif n1 > me and n2 > me and n3 <= me and n4 > me and n5 > me:
        return (f'''{n1:.2f}
{n2:.2f}
{n4:.2f}
{n5:.2f}''')
    elif n1 > me and n2 <= me and n3 > me and n4 > me and n5 > me:
        return (f'''{n1:.2f}
{n3:.2f}
{n4:.2f}
{n5:.2f}''')
    elif n1 <= me and n2 > me and n3 > me and n4 > me and n5 > me:
        return (f'''{n2:.2f}
{n3:.2f}
{n4:.2f}
{n5:.2f}''')
    else:
        return "Você não digitou números válidos"




def main():
    n1 = int(input())

    n2 = int(input())

    n3 = int(input())

    n4 = int(input())

    n5 = int(input())

    me = media(n1,n2,n3,n4,n5)

    ma = maior(n1,n2,n3,n4,n5)


    print(f'{me:.2f}')
    
    print(f'{ma}')


if __name__ == '__main__':
    main()

