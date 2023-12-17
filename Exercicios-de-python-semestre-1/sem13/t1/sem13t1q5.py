'''Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos, 
cujos elementos sejam a intercalação dos elementos de A e B.'''

def calc():

# a lista "l_geral" vai armazenar todos os numeros, e no loop eles serão filtrados e mandados para as listas "la" ou "lb"
    l_geral = []
    la = []
    lb = []

# nesse loop o usuário irá digitar 25 numeros e eles serão adicionados na lista "la"
    for i in range (25):
        n = int(input())
        la.append(n)
        
# nesse loop o usuário irá digitar 25 numeros e eles serão adicionados na lista "lb"        
    for x in range(25):
        v = int(input())
        lb.append(v)
        
# nesse outro loop, a cada iteraçã (25), um elemento de cada lista será adicionado na lista "l_geral", totalizando 50.        
    for _ in range(len(la)):
        l_geral.append(la[_])
        l_geral.append(lb[_])

# retorna as listas
    return f'{la}\n{lb}\n{l_geral}'

# imprime o retorno
print(calc())
