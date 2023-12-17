'''Leia um dia e um mês como números inteiros distintos e informe as cidades que fazem aniversário nessa data.
Veja o exemplo para o dia 9 e mês 2:
CIDADES QUE FAZEM ANIVERSÁRIO EM 9 DE FEVEREIRO:
São Miguel do Passa Quatro(GO)
Centralina(MG)
Itaporanga(PB)'''
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
