# Suas duas listas
numeros = [1, 2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd', 'e']

# Calcula a média da lista de números
media_numeros = sum(numeros) / len(numeros)

# Filtra os números maiores que a média
numeros_maiores_que_media = [num for num in numeros if num > media_numeros]

# Imprime os números maiores que a média
print("Números maiores que a média:", numeros_maiores_que_media)

# Encontra os índices dos números maiores que a média
indices_maiores_que_media = [numeros.index(num) for num in numeros_maiores_que_media]

# Filtra as letras com base nos índices encontrados
letras_correspondentes = [letras[indice] for indice in indices_maiores_que_media]

# Imprime as letras correspondentes
print("Letras correspondentes aos índices dos números maiores que a média:", letras_correspondentes)
