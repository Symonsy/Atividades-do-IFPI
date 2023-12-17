#  Escreva um programa que leia o nome e o estado civil de uma pessoa, considere apenas “1” para casado e “2” para solteiro. Se a pessoa for casada,
#  leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s) nome(s) lido(s).


# A variável "a" recebe os parâmetros "n", "ec", "c", que são nome, estado civil e conjuge, respecivamente.
def a(n, ec, c):
    
# Se "ec" fo igual a 1 (casado), retorna a quantidade de caracteres do nome da pessoa(n) e do cônjuge(c), senão retorna apenas o da pessoa.
    if ec == '1':
        return len(n) + len(c)
    else:
        return len(n)


# a variável "nome" recebe, em string, o nome da pessoa, que tem seus espaços em branco deletados
nome = str(input()).strip()

# A variável "estado_civil" recebe a entradp dp valor digitado pelo usuário, sendo “1” para casado e “2” para solteiro.
estado_civil = (input())

# Se a entrada do valor do valor do estado civil for um, pede para o usuário digitar o nome do conjuge, se não, a variável "cônjuge" fica vazia.
if estado_civil == '1':
    conjuge = str(input()).strip()
else:
    conjuge = ''.strip()

# A variável "result" chama a função "a" para execução com as variáveis "nome", "estado_civil" e "conjuge" sendo seus parâmetros.
result = a(nome, estado_civil, conjuge)

# A variável "result" é imprimida.
print(result)

