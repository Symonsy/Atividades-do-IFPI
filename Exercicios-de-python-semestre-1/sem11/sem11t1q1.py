'''01. Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança. Mostre
em quantos anos o valor acumulado será o dobro do valor inicial. Por exemplo:

R$100,00 rendendo 8% ao ano irá
dobrar em 10 anos.
Início R$ 100.00
1 ano R$ 108.00
2 anos R$ 116.64
3 anos R$ 125.97
4 anos R$ 136.05
5 anos R$ 146.93
6 anos R$ 158.69
7 anos R$ 171.38
8 anos R$ 185.09
9 anos R$ 199.90
10 anos R$ 215.89
'''

# a função 'dobro_val' recebe os parâmetros 'deposito_inicial' e 'taxa'
def dobro_val(deposito_inicial, taxa):

# a variável 'montante' é inicializada e recebe o valor do parâmetro 'depoósito inicial'e abaixo a variável 'anos' é inicializada com o valor zero para fazer a contagem dos anos
    montante = deposito_inicial
    anos = 0

# o loop é iniciado e é executado enquanto o montante for menor que o dobro do capital inicial, e adiconará mais uma ao ano enquanto for executado
    while montante < (deposito_inicial * 2):
        montante = montante * (1 + taxa / 100)
    
        anos += 1

# retorna o valor dos anos
    return anos


def main():
# as variáveis recebem o valor e a taxa que será aplicada 
    valor = float(input())
    taxa = float(input())

# a variavel 'res' chama a função pra execução com as variáveis 'taxa' e 'valor' como parâmetros, e armazena o resultado dessa função
    res = dobro_val(valor, taxa)

# imprime o resultado contido em 'res'
    print(res)
if __name__ == '__main__':
    main()