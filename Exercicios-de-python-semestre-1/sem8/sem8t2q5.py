# Função "mediafinal" calcula a média final e determina o conceito e resultado com base nos parâmetros de entrada.
def mediafinal(matr, n1, n2, n3, me):
    # Calcula a média final com a fórmula especificada.
    mf = (n1 + n2 * 2 + n3 * 3 + me) / 7

    # Verifica o conceito e o resultado com base na média final.
    if mf >= 9.0:
        return f'{matr}\n{mf:.2f}\nA\nAprovado'
    elif 7.5 <= mf < 9.0:
        return f'{matr}\n{mf:.2f}\nB\nAprovado'
    elif 6.0 <= mf < 7.5:
        return f'{matr}\n{mf:.2f}\nC\nAprovado'
    elif 4.0 <= mf < 6.0:
        return f'{matr}\n{mf:.2f}\nD\nReprovado'
    elif mf < 4.0:
        return f'{matr}\n{mf:.2f}\nE\nReprovado'

# Solicita os dados do aluno: matrícula, notas e média dos exercícios.
matricula = input()
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
media_exercicios = float(input())

# Chama a função "mediafinal" com os dados do aluno para calcular o conceito e o resultado.
resultado = mediafinal(matricula, nota1, nota2, nota3, media_exercicios)

# Imprime o resultado.
print(resultado)
