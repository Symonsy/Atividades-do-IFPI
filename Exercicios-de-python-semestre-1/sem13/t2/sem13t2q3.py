'''3. Escreva um programa que ler a nota de 50 alunos. Mostre uma lista apenas com os índices dos alunos que
tem nota maior ou igual a 6 (seis).'''



def calc():
# a lista "l1" armazena as motas dos alunos, e a lista "l2" os índices das notas maiores que 6.0
    l1 = []
    l2 = []

# nesse loop 50 notas serão recebidas e adicionadas na lista "l1"
    for i in range(50):
        val = float(input())
        l1.append(val)

# nesse o loop, na lista "l1", com a função "enumerate", irei percorrer todas as notas e seus índices na lista e os que forem maiores que 6 serão adicionados na lista "l2".     
    for indice, nota in enumerate(l1):
            if nota >= 6.0:
                l2.append(indice)

# retorna a lista  
    return l2

# imprime o retorno
print(calc())