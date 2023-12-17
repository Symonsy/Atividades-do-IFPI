# 04. A função 'converter' é criada com o parâmetro 'ano', que é definido pela leitura do valor digitado na variável 'idade_terrestre'. O valor final é imprimido com a execução da função 'converter' com a variável 'idade_terrestre' sendo seu parâmetro.

def converter(ano):
     
     idade_espacial = ano * (1/2)
     return int(idade_espacial)

idade_terrestre = int(input())
print(converter(idade_terrestre))


