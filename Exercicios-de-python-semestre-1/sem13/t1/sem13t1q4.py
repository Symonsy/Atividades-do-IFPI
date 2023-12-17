'''4. Leia 20 números inteiros e armazene-os numa lista. Separe os números pares na lista PAR e os números
ímpares na lista IMPAR. Imprima as três listas.'''


def e_par(x):
    return x % 2 == 0

def calc():

# a lista "l_geral" vai armazenar todos os numeros, e no loop eles serão filtrados e mandados para as listas "par" ou "ímpar"
    l_geral = []
    par = []
    imp = []

# nesse loop o usuário vai digitar 20 numeros eles serão adicionados na lista "l_geral", e a depender do resultado da função "e_par" eles serão adiconados nas listas "par" ou "ímpar"
    for i in range (20):
        n = int(input())
        l_geral.append(n)
        if e_par(n):
            par.append(n)
        else:
            imp.append(n)
        
# retorna as listas
    return f'{l_geral}\n{par}\n{imp}'

# imprime o retorno
print(calc())