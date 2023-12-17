'''
05. Faça um programa que leia a nota de um aluno, entre zero e dez. Mostre a mensagem “Nota inválida.”
caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. Após informar
uma nota válida, o aluno deve ver seu conceito, segundo a tabela:

Conceito     Nota
A             >= 8,5.
B             >= 7,0
C             >= 5,0
D             >= 4
E             >= 0
'''

# a função 'conceito' é criada
def conceito():

# a variável 'c' é criada para receber o conceito de acordo com a nota digitada, em maiúsculo
    c = ''.upper()

# o loop é iniciado e logo após alguma nota válida ser digitada ele encerra, e de acordo com essa nota o conceito do aluno é atribuído, mandado pra a variável 'c' e se a nota não for válida, exibe a mensagem 'Nota inválida'
    while True:

        nota = float(input())

        if 0 <= nota <= 10:
            if nota >= 8.5:
                c = 'A'
            elif nota >= 7.0:
                c = 'B'
            elif nota >= 5.0:
                c = 'C'
            elif nota >= 4.0:
                c = 'D'
            else:
                c = 'E'
            break
        else:
            print("Nota inválida.")
          
# retorna o conceito
    return f'{c}'

# imprime o resultado
print(conceito())