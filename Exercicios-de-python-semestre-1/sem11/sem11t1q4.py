'''
04. Escreva um programa que leia número inteiro qualquer e mostre na forma invertida. Por exemplo:
Para o número lido: 123, a saída será: 321
'''
# a função 'inverte' recebe o parâmetro 'val'
def inverte(val):

# armazena o número invertido
    numero_invertido = 0

# um loop é inciado
    while val > 0:

# os digitos são obtidos de tras pra frente, enquanto o valor for maior que zero, o último digito será obtido em uma divisão por 10
        digito = val % 10

# a cada iteração, o digito é multiplicado por 10 para organizar a fomratação, por exemplo: o número e 345, em uma iteração ja havia o valor 5 como o último, e o próximo numero a ser adicionado é 4, o 5 será multiplicado por 10 e ficará: 50 + 4 = 54, se não fose multiplicado por 10 iria ser 9. 
        numero_invertido = numero_invertido * 10 + digito

# o número é redefido para não sair digitos repetidos
        val //= 10

# retorna o numero depois do loop
    return numero_invertido

# recebe  numero a ser invertido
num = int(input())

# chama a função pra execução com 'num' sendo seu parâmetroe armazena seu valor
res = inverte(num)

# imrime o resultado
print(res)