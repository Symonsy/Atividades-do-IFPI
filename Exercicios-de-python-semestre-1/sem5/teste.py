def calc(pop):

    resultado = 0
    ano = 1599

    while pop > (pop * 0.1):
        nascimentosporano = int(pop * 0.01)
        mortesporano = int(pop * 0.06)
        populçaoporano = pop - mortesporano

        ano += 1
        resultado += (ano, nascimentosporano, mortesporano, populçaoporano)

    return resultado


pop = int(input())
res = calc(pop)

for ano, nascimentosporano, mortesporano, populçaoporano in res:
    print(f"{ano}, {nascimentosporano}, {mortesporano}, {populçaoporano}")
