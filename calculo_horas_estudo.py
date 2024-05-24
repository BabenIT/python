nome = str(input('Qual é seu nome:'))
print('Olá', nome , 'tudo bem?')
print('Calculo de tempo de estudo semanal')
valor2 = int(input("segunda-feira: "))
valor3 = int(input("terça-feira: "))
valor4 = int(input("quarta-feira: "))
valor5 = int(input("quinta-feira: "))
valor6 = int(input("sexta-feira: "))
valor7 = int(input("sabado: "))
valor1 = int(input("domingo: "))
total = valor1+valor2+valor3+valor4+valor5+valor6+valor7
print('total estudado na semana: ', total , 'minutos')
print('ou')
horas = total//60
minutos = total%60
print(horas,'horas', 'e' , minutos, 'minutos')
print ('Sua media diaria de estudo', nome, 'é', total/7, 'minutos')