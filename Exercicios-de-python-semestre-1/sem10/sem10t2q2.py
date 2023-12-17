'''
02. Modifique a canção dos programadores do exercício anterior para incluir o refrão: Tecle “Ctrl+F5”.

Termine a canção com “Vamos fazer mais um café!”.

99 bugs no software, pegue um deles e conserte...
Tecle “Ctrl+F5”
100 bugs no software, pegue um deles e conserte...
Tecle “Ctrl+F5”
101 bugs no software, pegue um deles e conserte...
Tecle “Ctrl+F5”
...
250 bugs no software, pegue um deles e conserte...
Tecle “Ctrl+F5”
Vamos fazer mais um café!
'''


# a função 'musica' é criada
def musica():

# a variavel versos é criada pra armazenar os versos da canção
    versos = ""

# as condicionais são criadas para que não haja quebra de linha no final do código e adicionar o final na proxiam linha.
    for i in range(98, 250):
        if i == 249:
            versos += f"{i+1} bugs no software, pegue um deles e conserte...\nTecle \"Ctrl+F5\"\nVamos fazer mais um café!"
        else:
            versos += f"{i+1} bugs no software, pegue um deles e conserte...\nTecle \"Ctrl+F5\"\n"

# retorna a varivel 'versos'
    return versos

# imprime a função
print(musica())


