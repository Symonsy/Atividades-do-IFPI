'''02. Escreva um programa que, para um número indeterminado de pessoas:
a. leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos dados (flag)
e não deve ser considerada;
b. calcule e escreva o número de pessoas;
c. calcule e escreva a idade média do grupo;
d. calcule e escreva a menor idade e a maior idade
'''

# a função 'dados' é criada sem parâmetro 
def dados():

# uma lsta é criada vazia pra armazenar os valores digitados pelo usuário
    idade = []

# o loop é iniciado pedindo um número inteiro para o usúario, e se ele for zero o loop é encerrado, mas antes disso todos os valores digitados antes do zero adicionados na lista
    while True:
        i = int(input())
        if i == 0:
            break
        idade.append(i)

# usando funções embutidas no python para manipular os valores da lista, obtive, respectivamente, a soma, a quantidade, a média, o menor e o maior valor da lista
    somaid = sum(idade)
    qtpessoa = len(idade)
    med_idade = somaid/ qtpessoa
    menor_id = min(idade)
    maior_id = max(idade)

# os valores são retornados na seguinte ordem: quantidade de pessoas, média idade, menor idade e maior idade  
    return f'{qtpessoa}\n{med_idade:.2f}\n{menor_id}\n{maior_id}'

# imprime os valores da função
print(dados())