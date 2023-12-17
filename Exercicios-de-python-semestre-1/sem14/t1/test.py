def calc():

    result = []
    names = []
    ages = []
    heights = []
    average = 0

    for i in range(30):
        
        name = str(input())
        names.append(name)
        
        age = int(input())
        ages.append(age)

        height = round(float(input()), 2)
        heights.append(height)

    average = sum(heights)/len(heights)

    for ind, i in enumerate(heights):  # Aqui está a mudança
        if i < average:
            a = ages[ind]
            n = names[ind]

            if a > 13:
                result.append(n)

    res = ("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA\n")

    for i in result:
        res += f'{i}\n'

    return (res).strip()

print(calc())