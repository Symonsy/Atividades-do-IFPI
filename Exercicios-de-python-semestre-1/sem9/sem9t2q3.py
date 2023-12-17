# Função para verificar se uma data é válida
def ver_data(data):
    # Verificar se a data é maior que 99999999 (8 dígitos no máximo)
    if data > 99999999:
        return False
    
    # Extrair o dia, mês e ano da data
    dia = data // 1000000
    mes = (data % 1000000) // 100
    ano = data % 10000

    # Converter os valores extraídos para inteiros (remover parte decimal, se houver)
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    # Verificar se o dia está no intervalo de 1 a 31 e o mês está no intervalo de 1 a 12
    if 1 <= dia <= 31 and 1 <= mes <= 12:
        return True
    else:
        return False

# Entrada de dados: o usuário insere uma data no formato DDMMAAAA
date = int(input("Digite uma data no formato DDMMAAAA: "))

# Processamento: chamando a função ver_data para verificar se a data é válida
result = ver_data(date)

# Saída de dados: exibir o resultado (True para data válida, False para data inválida)
print(result)
