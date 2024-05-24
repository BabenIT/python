# Faça um programa que leia a altura de uma pessoa em metros e o seu gênero (use 1 para feminino e 2 para masculino). A seguir, o programa deve escrever o peso ideal dessa pessoa conforme descrito a seguir: 
#para homens, o peso ideal corresponde a 72.7 x altura - 58
#para mulheres, use 62.1 x altura - 44.7

altura = float(input('digite sua altura em metros: '))
genero = int(input('digite seu genero masculino digite 1 e feminimo digite 2: '))

if genero == 1 : peso = altura * 72.7 -58
if genero == 2 : peso = altura * 62.1 -44.7
if genero !=1 and genero !=2 :
    print ("Genero invalido, peso ideal não calculado")

print("peso ideal: ", peso)