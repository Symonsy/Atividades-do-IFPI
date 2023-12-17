'''
05. Escreva um programa que leia três números inteiros correspondentes a três notas de um aluno. Apresente a média
das três notas, mas, se a terceira nota for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso,
se a média final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.

'''

# a função "m" recebe os parâmetros 'n1', 'n2', 'n3' como parâmetros correspondetes as notas do aluno.
def m(n1, n2, n3):

# a variável "media" recebe a media calculada com 2 casa decimais.
    media = round((n1 + n2 + n3) / 3, 2)
    
# Se a 3° nota for maior a média tem mais um ponto atribuido.
    if n3 > 8:
      media += 1

# se a média for maior que 10, ela é igualada a 10, pois esse é o limite.
      if media > 10:
         media  = 10
# retorna o valor final da média
    return media
          
# As próximas 3 variáveis recebem os valores das tres notas.      
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

# A variável "res" chama a função "m" para a execução com as 3 notas como parâmetros
res = m(nota1, nota2, nota3)

# A variável "res" é imprimida
print(f'{res}')

