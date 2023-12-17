'''
05. Escreva um programa que simula o valor (com duas casas decimais) da prestação de uma compra
parcelada sem juros de 1x até 24x. O valor da compra é digitado pelo usuário. O valor da prestação sem
juros, deve ser calculado como o valor da compra dividido pelo número de prestações de 1 até 24. O
programa estará correto se o usuário informar o valor 1000 e o programa produzir o seguinte resultado:

1x de R$ 1000.00
2x de R$ 500.00
3x de R$ 333.33
4x de R$ 250.00
5x de R$ 200.00
6x de R$ 166.67
7x de R$ 142.86
8x de R$ 125.00
9x de R$ 111.11
10x de R$ 100.00
11x de R$ 90.91
12x de R$ 83.33
13x de R$ 76.92
14x de R$ 71.43
15x de R$ 66.67
16x de R$ 62.50
17x de R$ 58.82
18x de R$ 55.56
19x de R$ 52.63
20x de R$ 50.00
21x de R$ 47.62
22x de R$ 45.45
23x de R$ 43.48
24x de R$ 41.67
'''


#processamento
def musica(val):

# a variável parcela é criada pra receber o resultado final
    parcela = ""

# a variável vezes é criada pra indicar a quantidade de parcelas, que é definida no range do 'for'
    vezes = 0

# a variável só foi criada pra melhorar a legibilidade do código
    total = val

# o loop de 24 vezes é criado 
    for _ in range(24):

# são criadas essas condicionais pra que não haja quebra de linha no final do código. note que não ha o '\n' no 'if' da variável parcela, mas no 'else' há, e també tem um ponto strip no retorno.        

# o numero de parcelas é definido adicionando '1' 24 vezes a variável 'vezes' e o valor da parcela é definido pela divisão do valor, que é a variável 'val', pelo número de vezes. 
        if vezes == 24:
            vezes +=1
            parcela += f"{vezes}x de R$ {total/vezes:.2f}"
            val= val/(vezes)
        else:
            vezes +=1
            parcela += f"{vezes}x de R$ {total/vezes:.2f}\n"
            val= val/(vezes)   
# retorna o resultado
    return parcela.strip()


# a variável 'val' recebe em float a entrada digitada pelo usuário
val = float(input())

# a variável 'res' manda a entrada pra digitada na variável 'res' pra função 'musica'.
res = musica(val)

# imprime 'res'
print(res)