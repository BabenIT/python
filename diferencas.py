import math
numero1 = int(input('Informe o primeiro numero: '))
numero2 = int(input('Informe o segundo numero: '))
print('a soma =' , numero1 + numero2)
print('a diferença =' , numero2 - numero1)
print('a media entre eles é: ', (numero1 + numero2)/2)
print('a distancia entre eles é: ', math.fabs(numero1-numero2))
print('o maior dos dois é: ', (numero1+numero2+math.fabs(numero1-numero2))/2)
print('o menor dos dois é: ', (numero1+numero2-math.fabs(numero1-numero2))/2)