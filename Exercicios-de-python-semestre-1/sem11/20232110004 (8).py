# 04. Escreva um programa que gere a seguinte sequência:
# 10, 20, 30, 40, ..., 990, 1000.
# Considere a separação dos números por vírgula seguido de espaço em branco e o ponto no final da
# sequência.


def num():
    numini = 10
    numeros = ''
    for n in range(100):
        if numini == 1000:
            numeros += str(numini) + '.'
        else:
            numeros += str(numini) + ', '
            numini +=10
    return  numeros

print(num())