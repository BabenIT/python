horaini = int(input('informe a hora inicial do jogo:'))
minutoini = int(input('informe a minuto inicial do jogo:'))
horaclo = int(input('informe a hora final do jogo:'))
minutoclo = int(input('informe a minuto final do jogo:'))

horarioini = horaini*60 + minutoini
horarioclo = horaclo*60 + minutoclo

if horarioini < horarioclo :
    duracao = horarioclo - horarioini

else:
    duracao = 24*60 - horarioini + horarioclo

print('Horas: ', duracao//60)
print('Minutos:', duracao%60)