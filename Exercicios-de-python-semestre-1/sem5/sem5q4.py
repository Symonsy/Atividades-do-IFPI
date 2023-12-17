# Escreva um programa que leia uma determinada quantidade de minutos e informe essa
# quantidade convertidade para horas e minutos.
# Por exemplo, 220 minutos é equivalente 3 horas e 40 minutos.
# OBS: Mostre o resultado na forma H:M

# A variável 'minutitos' é criada com o parâmetro 'minutos'recebido pela variável 'total' a partir da leitura do valor na variável minutos. Assim esse valor é convertido de horas pra minutos.

def minutitos(minutos):

    global horas
    global minut0s

    horas = minutos//60
    minut0s = minutos % 60

    return horas, minut0s


minutos = int(input())
total = minutitos(minutos)

print(f'{horas}:{minut0s}')
