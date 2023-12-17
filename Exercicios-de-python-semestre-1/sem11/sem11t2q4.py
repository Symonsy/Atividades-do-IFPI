'''04. O cardápio de uma casa de lanches, especializada em sanduíches, é dado abaixo.
CÓDIGO PRODUTO           PREÇO (R$)
H      Hamburger         5.50
C      Cheeseburger      6.80
M      Misto Quente      4.50
A      Americano         7.00
Q      Queijo Prato      4.00
X      PARA TOTAL DA CONTA

Escreva um programa que leia o código de vários itens comprados por um freguês e acumule o total da
compra. Ao finalizar com “X”, exiba o total a pagar.

Observações:
• Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção
inválida.”.
• Enquanto o código não for 'X' o programa deve continuar lendo os itens.

Dica: Use upper() para ignorar a diferenças entre maiúscula e minúsculas; Use [0] para garantir que
apenas o primeiro caractere digitado seja considerado. 

Por exemplo:
codigo = input('Código: ').upper()[0]
'''
# a função 'calc' é criada
def calc():

# a variável 'total' é criada para armazenar os valores dos produtos escolhidos pelo usuário
    total = 0

# a variável 'msg' é criada para armazenar o menu a cada iteração
    msg = ''

# o loop é iniciado com a condição de parada sendo c == 'X', e de acordo com as opções escolhidas anteriormente o preço é somado a variável 'total', e se o usuário escolher um código fora do menu a variável 'total' é convertida pra string e recebe a mensagem 'Opção inválida'
    while True:
        c = str(input().upper()[0])
        
        if c == 'H':
            total += 5.50
            msg += '''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA\n'''
        elif c == 'C':
            total += 6.80
            msg += '''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA\n'''

        elif c == 'M':
            total += 4.50
            msg += '''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA\n'''

        elif c == 'A':
            total += 7.00
            msg += '''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA\n'''

        elif c == 'Q':
            total += 4.00
            msg += '''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA\n'''

        elif c == 'X':
            msg += '''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA\n'''
            break
        else:
            total = str('Opção inválida.')

# retorna as variáveis após o loop com as suas respectivas formatações
    return f'{msg}{total:.2f}'

#imprime o resultado
print(calc())