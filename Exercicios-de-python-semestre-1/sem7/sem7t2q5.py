# 05. Escreva um programa que leia três números e mostre na tela em ordem crescente.

# A função "n" recebe três valores, "v1", "v2" e "v3", e os organiza em ordem crescente.
def n(v1, v2, v3):
    
    # Verifica todas as possíveis combinações de ordem crescente e retorna os números ordenados.
    if v1 <= v2 <= v3:
        return f"{v1}\n{v2}\n{v3}"
    elif v1 <= v3 <= v2:
        return f"{v1}\n{v3}\n{v2}"
    elif v2 <= v1 <= v3:
        return f"{v2}\n{v1}\n{v3}"
    elif v2 <= v3 <= v1:
        return f"{v2}\n{v3}\n{v1}"
    elif v3 <= v1 <= v2:
        return f"{v3}\n{v1}\n{v2}"
    else:
        return f"{v3}\n{v2}\n{v1}"

# Solicita três números ao usuário.
n1 = int(input())
n2 = int(input())
n3 = int(input())

# Chama a função "n" com os valores fornecidos e armazena o resultado.
res = n(n1, n2, n3)

# Imprime os números em ordem crescente.
print(res)
