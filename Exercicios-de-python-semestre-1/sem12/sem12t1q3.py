'''
02. Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3%
ano. Sabe-se que, atualmente, o país A tem população maior que o país B. Faça um programa que leia a
população de cada país e imprima o tempo necessário para que a população do país B ultrapasse a
população do país A.
'''

def calc(pa, pb):
    t = 0  # Inicializa a variável de tempo.

    # Verifica se a população de A é maior que a de B.
    if pa > pb:
        while pa > pb:  # Enquanto a população de A for maior que a de B, continue o loop.
            pa = pa * (1.02)  # A população de A aumenta 2% ao ano.
            pb = pb * (1.03)  # A população de B aumenta 3% ao ano.
            t += 1  # Incrementa o tempo em 1 ano a cada iteração.

    # Caso contrário, se a população de B já for maior que a de A.
    else:
        while pa < pb:  # Enquanto a população de A for menor que a de B, continue o loop.
            pa = pa * (1.03)  # A população de A aumenta 3% ao ano.
            pb = pb * (1.02)  # A população de B aumenta 2% ao ano.
            t += 1  # Incrementa o tempo em 1 ano a cada iteração.

    return t  # Retorna o tempo necessário para que a população de B ultrapasse a população de A.

# Solicita a população de B e A ao usuário.
p_b = float(input("Digite a população do país B: "))
p_a = float(input("Digite a população do país A: "))

# Chama a função 'calc' com as populações fornecidas e armazena o resultado em 'res'.
res = calc(p_a, p_b)

# Imprime o resultado, ou seja, o tempo necessário para a população de B ultrapassar a população de A.
print("Tempo necessário para B ultrapassar A:", res, "anos")
