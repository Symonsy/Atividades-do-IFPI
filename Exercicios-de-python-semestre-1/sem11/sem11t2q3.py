
# a função serviço é criada
def serviço():

 # a variável 'res' armazenara o resultado de acordo com a opção escolhida   
    res = ''

# o loop é iniciado com a condição de parada sendo a variável 'opção' igual a 0. O valor digitado é recebido e de acordo com as condições, a variável 'res' é somada, e definida como mais aquela opção.
    while True:
        opção = int(input())
        if opção == 3:
            res += 'OPÇÕES:\n1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM\n3 - Meus Parabéns!\n'
        elif opção == 2:
            res += 'OPÇÕES:\n1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM\n2 - Vamos estudar mais.\n'
        elif opção == 1:
            res += 'OPÇÕES:\n1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM\n1 - Olá. Como vai?\n'
        elif opção == 0:
            res += 'OPÇÕES:\n1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM\n0 - Fim de serviço.\n'
            break
        else:
            res += 'OPÇÕES:\n1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM\nOpção inválida.\n'

# retorna a variável 'res' sem as quebras de linha do final
    return res.strip()

# imprime o resultado obtido
print(serviço())