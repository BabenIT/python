print('informe o tempo do evento em segundos: ')
tempo = int(input())
hora = tempo//3600
print('Horas', hora)
resto = tempo%3600
minutos = resto//60
print('Minutos', minutos)
segundos = resto%60
print('Segundos: ' , segundos)