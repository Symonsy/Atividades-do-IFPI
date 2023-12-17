'''Escreva um programa que ler dois conjuntos de números reais, armazenando-os em listas e calcule o produto escalar entre eles. Os conjuntos têm 5 elementos cada. 
Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar e dado por: (x1*y1 )+(x2*y2 )+(x3*y3 )+⋯+(xn*yn). Por exemplo, para as duas listas X e Y a seguir:

        0       1       2       3       4
X =     2       5       7       3       9
Y =     3       8       1       0       4

O produto escalar será: (2 x 3) + (5 x 8) + (7 x 1) + (3 x 0) + (9 x 4) = 89'''
def calc():
    l1 = [] # armazenará o 1° conjunto de números
    l2 = [] # armazenará o 2° conjunto de números
    l3 = [] # armazenará o produto dos elementos correspondentes em l1 e l2

# os dois próximos loops servirão para receber e adicionar os elementos dos conjuntos 1 e 2
    for _ in range(5):
        num = int(input())
        l1.append(num)

    for _ in range(5):
        num = int(input())
        l2.append(num)

# a cada iteração são calculados os produtos dos elementos dos 2 conjuntos e são armazenados na 3° lista
    for i in range(5):
        l3.append(l2[i]*l1[i])
        
    res = str()
    ind = 0

# em cada iteração do loop, de acordo com o índice, que é a variável "ind"( e a cada iteração será adicionado mais 1, percorrendo assim todos os índices dos conjuntos 1 e 2), os elementos de "l1" e "l2" são adicionados na variável "res".
    for i in range(len(l2)):
        res += '(' + str(l1[ind]) + " " + 'x' + " " + str(l2[ind]) + ')' + " ""+"" "
        ind +=1

# aqui o produto escalar é calculado
    p = sum(l3)

    res = res[:-3] # após o loop os últimos 3 caracteres de "res", que são: " + ", são removidos 
    
# os dois conjuntos são retornados, junto com a representação da operação para calcular o produto escalar, que é a variável res, e o produto escalar    
    return f'{l1}\n{l2}\n{res} = {p}'

# o retorno é imprimido
print(calc())
