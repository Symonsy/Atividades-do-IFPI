'''02.Faça um programa que receba a temperatura média de cada mês do ano. A temperatura pode ser informada em graus
Celsius, Fahrenheit ou Kelvin. Após isto, calcule a média anual das temperaturas e mostre, em Kelvin, todas as
temperaturas acima da média anual e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
Fevereiro, ... )'''

def calc():
    matriz = []

    for lin in range(12):
        lin = []
        for col in range(1):
            x = int(input())
            lin.append(x)

        matriz.append(lin)
