# Escreva um programa que leia um preço e um valor percentual. Informe o preço acrescido do percentual e o
# preço com o desconto percentual. Por exemplo, se for lido um preço de 100.00 e um valor percentual de 5.00 o
# programa deve mostrar que o preço com aumento é 105.00 e o preço com desconto é 95.00.
# OBS: Mostre sempre duas casas decimais.


# A função 'precinho' é criada com os parâmetros 'preço','v_p', que são recebidos pelas váriaveis 'preç' e 'valor_percentual' para serem calculados dentro da função e depois imprimidos na seguinte ordem: preço com aumento e depois desconto.

def precinho(preço, v_p):
    percentual = preço * v_p/100
    global v_au
    global v_di
    v_au = float(preço + percentual)
    v_di = float(preço - percentual)

    return v_au, v_di


def main():

    preç = float(input('digite o preço: '))
    valor_percentual = float(input('digite o percentual: '))

    precinho(preç, valor_percentual)

    print(f'{v_au:.2f}\n{v_di:.2f}')


if __name__ == "__main__":
    main()
