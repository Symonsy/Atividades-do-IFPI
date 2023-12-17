'''
3. Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro)
casas decimais.
b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa
decimal. Se n = 0, imprima “SEM NOTAS”.
c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.
Dica: certifique-se de ler apenas um caractere com input()[0] '''



# criei uma função para cada alternativa
# não consegui arredondar os valores na letra a), pelo visto não tem como.

# em um intervalo "n", o usuário irá digitar "n" números, e a acada iteração eles serão adicionados na lista "l1" na posição "0" fazendo com que os que foram digitados antes sejam "empurrados" pra direita, "invertendo" a lista.
def letraA(n):
    
    l1 = []
    for _ in range(n):
        i = float(input())
        i = round(i, 4)
        l1.insert(0, i)

# retorna a lista
    return l1

# em um intervalo "n", o usuário irá digitar "n" notas elas serão adicionadas a lista "l2", após isso a variável "m" receberá a média atraves da soma dos valores< -sum(l2)- dividido pela sua quantidade -len(l2)-, e a lista e a nota seram retornadas, ambas com 2 casas decimais 
def letraB(n):
   
    l2 = []

    for i in range(n):
        i = float(input())
        l2.append(i)

    m = sum(l2)/len(l2)

    return f'{l2}\n{m:.1f}'



def letraC(n):

# a lista "_13v" vai armazenar as vogais e a lista "_13c" as consiantes
    _l3v = []
    _l3c = []


# em um ntervalo "n", o usuário irá digitar "n" caracteres redigidos em minúsculos, e se for uma vogal irá par a lista "_l3v", se não, vai pra "_l3c". A variável "qt_l3v" vair recebr o tanto de caracteres/vogais da lista "_13v". As consoantes serão retornadas junto com a variável "m".
    for i in range (n):
        le = str(input())
        le = le.lower()[0]
        if le in "aeiou":
            _l3v.append(le)
        else:
            _l3c.append(le)

    qt_l3v = len(_l3v)        
    
    return f'{qt_l3v}\n{_l3c}'


def main():
# o valor "n" é recebido e mandado pras funções
    val_n = int(input())
    res1 = letraA(val_n)
    res2 = letraB(val_n)
    res3 = letraC(val_n)
    
# os resultados das funções são imprimidas    
    print(f'{res1}\n{res2}\n{res3}')

if __name__=="__main__":
    main()