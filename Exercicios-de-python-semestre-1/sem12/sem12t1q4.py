'''
03. O número da sorte de uma pessoa é calculado somando os dígitos da sua data de nascimento. Escreva um
programa que leia a data de nascimento, digitada no formado ddmmaaaa (um número inteiro com 8
dígitos), e mostre o seu número da sorte. Por exemplo, quem nasceu em 29/04/1989 deve digitar 29041989
e o programa vai calcular que o número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42)
'''

def calc(ds):

    # Inicializa a variável que vai armazenar o número da sorte.
    ns = 0

    # Enquanto a data de nascimento for maior que zero, continuamos a somar os dígitos.
    while ds > 0:
        
        # Pega o último dígito da data de nascimento e o adiciona ao número da sorte.
        ns += ds % 10

        # Remove o último dígito da data de nascimento para prosseguir com o próximo.
        ds //= 10
    
    # Retorna o número da sorte calculado.
    return ns

# Recebe a data de nascimento como um número inteiro.
data = int(input())

# Chama a função para calcular o número da sorte e armazena o resultado.
res = calc(data)

# Imprime o número da sorte.
print(res)
