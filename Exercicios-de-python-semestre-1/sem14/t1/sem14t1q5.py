'''5. Foram anotados nomes, idades e alturas de 30 alunos. Faça um programa que determine quais
alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos. Considerar a
altura arredondando para duas casas decimais.'''

def calc():

    result = [] # armazenará os nomes dos alunos maiores que a média
    names = [] # armazenará os nomes de todos os alunps 
    ages = [] # armazenará as idades de todos os alunos
    heights = [] # armazenará as alturas de todos os alunos
    average = 0 # armazenará a média das alturas

# nesse loop os nomes, as idades as alturas serão recebidos, e serão adiocionados nessa ordem ás listas "names", "ages" e "heights". E após isso a variável "average" vai recebr a média das idades
    for i in range(30):
        
        name = str(input())
        age = int(input())
        height = round(float(input()), 2)

        names.append(name)
        ages.append(age)
        heights.append(height)

    average = sum(heights)/len(heights)

# a cada iteração desse loop, a idade do aluno é comparada com 13, se for menor a variável "a" localizará a idade do aluno em questão na lista "ages" pelo índice de "i" na lista de alturas "heights" o mesmo pra variável "n", só que com o nome. E se a idade do aluno for maior que 13 o nome dele será adicionado na lista "result"
    for ind, i in enumerate(heights):
        if i < average:
            a = ages[ind]
            n = names[ind]

            if a > 13:
                result.append(n)

# a variável "res" receberá cada elemento da lista "result" a partir do loop a seguir, depois essa variável será retornada e impressa
    res = ("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA\n")

    for i in result:
        res += f'{i}\n'

    return (res).strip()

print(calc())
