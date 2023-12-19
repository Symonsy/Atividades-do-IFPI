'''02.Faça um programa que receba a temperatura média de cada mês do ano. A temperatura pode ser informada em graus
Celsius, Fahrenheit ou Kelvin. Após isto, calcule a média anual das temperaturas e mostre, em Kelvin, todas as
temperaturas acima da média anual e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
Fevereiro, ... )'''

def calc():
    anos = []
    temperaturas = []
    meses = [
        "Janeiro: "
        "Fevereiro: "
        "Março: "
        "Abril: "
        "Maio: "
        "Junho: "
        "Agosto: "
        "Setembro: "
        "Outubro: "
        "Novembro: "
        "Dezembro: "
    ]

    for mes in range(3):
        mes = []
        for col in range(1):
            temp = int(input())
            esc = str(input().upper())
            mes.append(temp, esc)
            if esc == "F":
                temp = (temp + 459.67) * 5/9
            elif esc == "C":
                temp = temp + 273.15

        anos.append(mes)
        temperaturas.append(temp)

    
    media = sum(temperaturas)/len(temperaturas)

    temps_acima_média = []

    for i in temperaturas:
        if i > media:
            ind = temperaturas.index(i)
            temps_acima_média.append(meses[ind]+temperaturas[ind]+"K")

    print("TEMPERATURA MÉDIA ANUAL")
    print(media,"K")
    print("TEMPERATURAS ACIMA DA MÉDIA ANUAL:")
    for i in temps_acima_média:
        print(f'{i}\n')

def main():
    calc()

if __name__=="__main__":
    main()