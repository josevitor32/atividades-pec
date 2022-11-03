anos = int(input('digite seus anos de idade: '))
meses = int(input('digite os meses: '))
dias = int(input('digite os dias: '))
total = (anos * 365) + (meses * 30) + dias
print('sua idade em dias é {} dias'.format(total))
