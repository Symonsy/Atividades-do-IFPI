# 05. A função 'temp' é criada com o parâmetro 'valor', que é definido pela leitura do valor digitado na variável de fora da função 'temp_cel', e essa mesma variável chama a função para a execução e depois é imprimida através da interpolação de strings, com o valor tendo duas casas decimais.

def temp(valor):
    temp_far = float((valor * (9/5))+32)
    return temp_far

temp_cel = float(input())
temp_cel = temp(temp_cel)
print(f'{temp_cel:.2f}')

