'''

O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal. O IMC é determinado pela divisão da 
massa do indivíduo pelo quadrado de sua altura, em que a massa está em quilogramas e a altura em metros. Escreva um programa que leia a massa (o peso) 
e a altura de uma pessoa e calcula o IMC de uma pessoa, e depois, mostra uma das seguintes mensagens:

IMC	Classificação
< 18,5	Abaixo do peso
< 25	Peso normal
< 30	Sobrepeso
< 35	Obeso leve
< 40	Obeso moderado
>=40	Obeso mórbido

'''
def imc(p, a):
    ngc = p/ a**2
    return f'{ngc:.2f}'


def estimc(p, a):
    ngc = p/ a**2

    if ngc < 18.5:
        return "Abaixo do peso"
    if ngc < 25:
        return "Peso normal"
    if ngc < 30:	
        return "Sobrepeso"
    if ngc < 35:
        return "Obeso leve"
    if ngc < 40:
        return "Obeso moderado"
    if ngc >= 40:
        return "Obeso mórbido"
    

m = float(input())
a = float(input())

res = estimc(m, a)
res2 = imc(m, a)

print(res2)
print(res)