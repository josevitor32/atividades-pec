def dados(população_original):
    a = 1600
    n = 0
    m = 0
    população_total = população_original
    while população_total > ((10 * população_original) / 100):
        m = ((6 * população_total) / 100)
        n = ((1 * população_total) / 100)
        população_total = população_total - (m - n)
        a += 1
        print(f'{a:.0f},{n:.0f},{m:.0f},{população_total:.0f}')

              

def main():
    população_original = int(input('Digite a população de aves: '))
    
    d = dados(população_original)
    

if __name__ == '__main__':
    main()
