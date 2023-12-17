# A função "imc" recebe a massa (peso) e altura de uma pessoa, calcula o índice de massa corporal (IMC)
# e o retorna formatado com duas casas decimais.
def imc(p, a):
    # Calcula o IMC dividindo a massa pelo quadrado da altura
    ngc = p / a**2
    return f'{ngc:.2f}'

# A função "estimc" recebe a massa (peso) e altura de uma pessoa, calcula o IMC e determina a classificação
# de acordo com os intervalos fornecidos, retornando a classificação correspondente.
def estimc(p, a):
    # Calcula o IMC dividindo a massa pelo quadrado da altura
    ngc = p / a**2

    # Verifica em qual intervalo o IMC se encontra e retorna a classificação correspondente
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

# Solicita a massa (peso) e altura da pessoa ao usuário.
m = float(input())
a = float(input())

# Chama a função "estimc" com a massa e altura fornecidas para obter a classificação do IMC.
res = estimc(m, a)

# Chama a função "imc" com a massa e altura fornecidas para obter o valor do IMC formatado.
res2 = imc(m, a)

# Imprime o valor do IMC e sua classificação.
print(res2)
print(res)
