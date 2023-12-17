
def dif(n1, n2, n3):
    resdif = 0

    if abs(n1 - n3) < abs(n1 - n2):
        resdif = abs(n1 - n3)
    else:
        resdif = abs(n1 - n2)

    return f'{resdif}'

# entrada
v1 = int(input().strip())
v2 = int(input().strip())
v3 = int(input().strip())

# processamento
res = dif(v1, v2, v3)

# saída
print(res)
