# Função para classificar a pessoa
def process(r1, r2, r3, r4, r5):
    res1 = 0  # Variável para contar o número de respostas "S"
    res2 = '' # Variável para armazenar a classificação final

    # Verificando a resposta da primeira pergunta
    if r1 == 'S':
        res1 += 1
    elif r1 == 'N':
        res1 += 0

    # Verificando a resposta da segunda pergunta
    if r2 == 'S':
        res1 += 1
    elif r2 == 'N':
        res1 += 0

    # Verificando a resposta da terceira pergunta
    if r3 == 'S':
        res1 += 1
    elif r3 == 'N':
        res1 += 0

    # Verificando a resposta da quarta pergunta
    if r4 == 'S':
        res1 += 1
    elif r4 == 'N':
        res1 += 0

    # Verificando a resposta da quinta pergunta
    if r5 == 'S':
        res1 += 1
    elif r5 == 'N':
        res1 += 0

    # Classificando a pessoa com base no número de respostas "S"
    if res1 == 0:
        res2 = 'Inocente'
    elif res1 == 2:
        res2 = 'Suspeito'
    elif 3 <= res1 <= 4:
        res2 = 'Cúmplice'
    elif res1 > 4:
        res2 = 'Assassino'

    return res2

# Solicitando as respostas para as perguntas
q1 = input("a) Telefonou para a vítima? (S/N): ").upper()
q2 = input("b) Esteve no local do crime? (S/N): ").upper()
q3 = input("c) Mora perto da vítima? (S/N): ").upper()
q4 = input("d) Devia para a vítima? (S/N): ").upper()
q5 = input("e) Já trabalhou com a vítima? (S/N): ").upper()

# Chamando a função de classificação e armazenando o resultado
result = process(q1, q2, q3, q4, q5)

# Exibindo a classificação final
print(f"A classificação da pessoa é: {result}")
