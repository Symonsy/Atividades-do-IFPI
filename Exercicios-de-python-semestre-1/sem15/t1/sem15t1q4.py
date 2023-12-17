'''04. Leia uma população e informe as cidades com população maior que o valor lido. Veja o exemplo:
Veja o exemplo para a leitura de 50000 para a população:

CIDADES COM MAIS DE 50000 HABITANTES:
IBGE: 120040 - Rio Branco(AC) - POPULAÇÃO: 290639
IBGE: 270030 - Arapiraca(AL) - POPULAÇÃO: 202398
IBGE: 270040 - Atalaia(AL) - POPULAÇÃO: 50323
...
'''
def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
                )
    arquivo.close()
    return resultado


def main():

    cidades = carrega_cidades()

    populacao = int(input())

    res = f"CIDADES COM MAIS DE {populacao} HABITANTES:\n"
    for cidade in cidades:
        if cidade[5] > populacao:
            res += f"IBGE: {cidade[1]} - {cidade[2]}({cidade[0]}) - POPULAÇÃO: {cidade[5]}\n"

    print(res.strip())

if __name__ == "__main__":
    main()


def main():

    cidades = carrega_cidades()

    dia = int(input())
    mes = int(input())
    messs = "" 
    
    if (mes == 1):
        messs = "JANEIRO"
    elif (mes == 2):
        messs = "FEVEREIRO"
    elif (mes == 3):
        messs = "MARÇO"
    elif (mes == 4):
        messs = "ABRIL"
    elif (mes == 5):
        messs = "MAIO"
    elif (mes == 6):
        messs = "JUNHO"
    elif (mes == 7):
        messs = "JULHO"
    elif (mes == 8):
        messs = "AGOSTO"
    elif (mes == 9):
        messs = "SETEMBRO"
    elif (mes == 10):
        return "OUTUBRO"
    elif (messs == 11):
        mes = "NOVEMBRO"
    elif (messs == 12):
        messs = "DEZEMBRO"
    
    res = f"CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {messs}:\n"
    for cidade in cidades:
        if cidade[3] == dia and cidade[4] == mes:
            res += f"{cidade[2]}({cidade[0]})\n"

    print(res.strip())

if __name__ == "__main__":
    main()

