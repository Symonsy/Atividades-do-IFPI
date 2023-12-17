# A função "val" recebe um número inteiro como entrada.
def val(num):
    # Verifica se o número está no intervalo entre 0 (exclusivo) e 100.000 (exclusivo).
    if 0 < num < 100000:
        # Converte o número em uma string para percorrer seus dígitos.
        novonum = str(num)
        # Inicializa uma variável "soma" para armazenar a soma dos dígitos.
        soma = 0

        # Itera por cada algarismo na string "novonum".
        for algarismos in novonum:
            # Converte o algarismo de volta para inteiro e adiciona à soma.
            soma += int(algarismos)

        # Retorna a soma dos dígitos.
        return soma
    # Verifica se o número é igual a zero.
    if num == 0:
        return "0"
    # Se o número não estiver no intervalo válido (0 a 100.000) e não for zero, retorna -1.
    else:
        return -1

# Solicita um número inteiro ao usuário.
numero = int(input())

# Chama a função "val" com o número fornecido para calcular a soma dos dígitos.
res = val(numero)

# Imprime o resultado da operação.
print(res)
