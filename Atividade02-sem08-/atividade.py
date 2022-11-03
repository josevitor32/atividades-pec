#O programa recebe uma data de nascimento, e imprime na tela o horoscopo diário de acordo com o signo do usuário por meio de um site.
def signo(dia,mes):#analisa o signo de acordo com o dia e o mês de nascimento informado pelo usuário e separados na função "separar_data".
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Aries'
    if mes == 4:
        return 'Aries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 22 else 'Gêmeos'
    if mes == 6:
        return 'Gêmeos' if dia < 23 else 'Câncer'
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sagitário'
    if mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricórnio'
    if mes == 11:
        return 'Capricórnio' if dia < 20 else 'Aquário'
    if mes == 12:
        return 'Aquário' if dia < 21 else 'Peixes'

def horoscopo(signo_desejado):
    import urllib.request, ssl #importa biblioteca para abrir urls.

    signo_formatado = remover_acentos(signo_desejado).lower() #recebe o signo e converte as letras para minúsculo.
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    requisicao = urllib.request.Request( #Recupera o conteúdo de uma URL.
        url=minha_url,
        headers={'User-Agent':'Mozilla/5.0'}
    )
    
    contexto_ssl = ssl.create_default_context()
    contexto_ssl.check_hostname = False
    contexto_ssl.verify_mode = ssl.CERT_NONE

    resposta = urllib.request.urlopen(requisicao, context=contexto_ssl)

    pagina = resposta.read().decode('utf-8')

    marcador_inicio = '<p class="text-pred">' #define onde deve começar e terminar o texto a ser impresso para o usuário.
    marcador_final = '<a class="webshare-link">Compartilhar</a>'

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return signo_desejado + ': ' + pagina[inicio:final].strip()

def separar_data(dma): #A função "separa_data(dma)",separa a data de nascimento informada pelo usuário, retornando o dia, mês e ano. 
    a = dma % 10000    #Com isso, é possível identificar o signo através da função "signo(dia,mes)".
    dma //= 10000

    m = dma % 100
    dma //= 100

    d = dma
    return d, m, a


def remover_acentos(texto):
    from unicodedata import normalize

    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

def main():
    nascimento = int(input('Digite sua data de nascimento no formato DDMMAAAA: '))

    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)

    print(horoscopo_de_hoje)

if __name__ == '__main__':
    main()
    
