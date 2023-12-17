'''
05. Pedro recebe um salário mensal e tem aumentos salariais de 5% uma vez por ano no mês de março. Pedro
também tem uma dívida no cartão de crédito com uma taxa de juros de 15% ao mês. Considerando que a
situação se refere ao mês de outubro do ano de 2016, estou fazendo um programa leia o valor do salário e o valor
da dívida e calcula, simulando a evolução do salário e da dívida de Pedro, em que mês e ano a dívida com
o cartão de crédito será superior ao seu próprio salário.

vou representar os meses como inteiros de 1 a 12.

pra me auxiliar melhor usei essas variáveis:
“dívida” que aumenta todo mês;
“salário” que aumenta apenas se o número do mês for 3 (março);
“mês” que é incrementado sempre, mas que retorna a 1 quando passar de 12;
“ano” que só é incrementado quando o mês retornar a 1.

Por exemplo: Considerando que o salário inicial é de R$ 2.000,00 e o valor da dívida é R$ 100,00 o valor
da dívida irá superar o salário em setembro de 2018 (9/2018)
'''

# a função 'calc' é iniciada com os parâmetros enviados
def calc(sal, div):

# a data inicial é stabelecida    
    ano = 2016
    mes  = 10
    
# um loop é iniciado e será terminado até que a divida seja maior que o salário    
    while div < sal:

# se o mes for três um bônus de 5% será aplicado ao salário
        if mes == 3:
            sal *= 1.05

# a cada iteração, ou seja, a cada mês, a divida é recalculada com uma taxa de 15% sob regime de juros composto e mais uma unidade é adiconada ao ano
        div *= 1.15 
        mes +=1

# quando o mês passar de 12, srá igualado a 1, e quando o mês for 1, mais 1 será incrementado ao ano.
        if mes > 12:
            ano += 1
            mes = 1

# retorna o mês e o ano calculados
    return f'{mes}/{ano}'


# as variáveis recebem o salário e a divida, respectivamente
s = float(input())
d = float(input())

# chama a função pra execução com 's' e 'd' sendo seus parâmetros e armazena seu valor
res = calc(s, d)

# imrime o resultado
print(res)