'''
04. Modifique mais um vez a canção dos programadores, dessa vez, gerando a canção dos bons
programadores, que resolvem 11 erros de cada vez e ao chegar a zero declaram que o software está
estabilizado. Atenção para o exemplo a seguir, especialmente, os versos finais.
99 bugs no software, pegue onze deles e conserte...
Tecle “Ctrl+F5”
88 bugs no software, pegue onze deles e conserte...
Tecle “Ctrl+F5”
77 bugs no software, pegue onze deles e conserte...
Tecle “Ctrl+F5”
...
11 bugs no software, pegue onze deles e conserte...
Tecle “Ctrl+F5”
Sem erros no software! Está estabilizado!
'''


def musica():

# a variável 'versos' é criada para armazenar os versos da canção.
    versos = ""

# a variável 'i' recebe o valor inteiro 99
    i = 99
    
# o loop de 9 vezes é criado    
    for _ in range(9):

# as condicionais são criadas para que não haja quebra de linha no final do código 

# ou seja quando i for subraído até 11, esse vais ser o valor da variável parrcela, senão vai ser outro
        if i == 11:
            versos += f"{i} bugs no software, pegue onze deles e conserte...\nTecle \"Ctrl+F5\"\nSem erros no software! Está estabilizado!"
            i -= 11
        else:
            versos += f"{i} bugs no software, pegue onze deles e conserte...\nTecle \"Ctrl+F5\"\n"
            i -= 11

#retorna o resultado
    return versos

#imprime o resultado da função
print(musica())


