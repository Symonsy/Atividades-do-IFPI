'''01. Escreva um programa que leia um número e exiba o dia correspondente da semana. (1-domingo, 2-segunda-feira,
3-terça-feira etc.), se digitar outro valor deve aparecer “valor inválido”.'''

def ver(val):


# verfifica o valor do dia e retorna a mensagem de acordo
    if val == 1:
        return 'domingo'
    if val == 2:
        return 'segunda-feira'
    if val == 3:
        return 'terça-feira'
    if val == 4:
        return 'quarta-feira'
    if val == 5:
        return 'quinta-feira'
    if val == 6:
        return 'sexta-feira'
    if val == 7:
        return 'sábado'
    else:
        return 'valor inválido'

# entrada

dia = int(input())

# processamento 

res = ver(dia)

# saída

print(res)


