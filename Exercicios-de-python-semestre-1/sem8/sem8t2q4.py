# A função "pesid" recebe a altura (a) e o sexo (s) como entrada.
def pesid(a, s):
    # Inicializa a variável de peso.
    peso = 0

    # Verifica o sexo (1 para homens, 2 para mulheres) e calcula o peso ideal.
    if s == 1:
        peso = (72.7 * a) - 58
    elif s == 2:
        peso = (62.1 * a) - 44.7

    # Formata o resultado com duas casas decimais e o retorna como string.
    return f'{peso:.2f}'

# Solicita a altura e o sexo ao usuário.
altura = float(input())
sexo = int(input())

# Chama a função "pesid" com a altura e o sexo fornecidos para calcular o peso ideal.
resultado = pesid(altura, sexo)

# Imprime o resultado.
print(resultado)
