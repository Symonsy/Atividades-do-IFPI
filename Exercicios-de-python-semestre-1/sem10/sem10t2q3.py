'''Modifique a canção dos programadores novamente para aumentar os bugs de 7 em 7, iniciando em 99 e
parando em 250 ou antes
99 bugs no software, pegue sete deles e conserte...
Tecle “Ctrl+F5”
106 bugs no software, pegue sete deles e conserte...
Tecle “Ctrl+F5”
113 bugs no software, pegue sete deles e conserte...
Tecle “Ctrl+F5”
...
Vamos fazer mais um café!
'''

def musica():

# a variavel versos é criada pra armazenar os versos da canção
    versos = ""

# um loop de 151 vezes é criado com passo 7
    for i in range(98, 250, 7):

# as condicionais são criadas para que não haja quebra de linha no final do código e adicionar o final na proxiam linha.
        if i == 249:
            versos += f"{i+1} bugs no software, pegue sete deles e conserte...\nTecle \"Ctrl+F5\"\nVamos fazer mais um café!"
        else:
            versos += f"{i+1} bugs no software, pegue sete deles e conserte...\nTecle \"Ctrl+F5\"\n"
    versos += "Vamos fazer mais um café!"
# retorna a varivel 'versos'
    return versos

# imprime a função
print(musica())

