def data_nascimento(data):
    while True:
        if len(data) == 8:
            d1 = int(data[0])
            d2 = int(data[1])
            m1 = int(data[2])
            m2 = int(data[3])
            a1 = int(data[4])
            a2 = int(data[5])
            a3 = int(data[6])
            a4 = int(data[7])
            return (d1 + d2 + m1 + m2 + a1 + a2 + a3 + a4)
        if len(data) == 7:
            d1 = int(data[0])
            d2 = int(data[1])
            m1 = int(data[2])
            m2 = int(data[3])
            a1 = int(data[4])
            a2 = int(data[5])
            a3 = int(data[6])
            return (d1 + d2 + m1 + m2 + a1 + a2 + a3)
        break
            

        

def main():
    data = input()
    
    d = data_nascimento(data)

    print(d)

if __name__ == '__main__':
    main()
