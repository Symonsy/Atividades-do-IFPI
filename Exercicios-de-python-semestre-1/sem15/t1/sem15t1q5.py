'''05. Leia um mês e uma população. Mostre as cidades com população maior que o valor lido fazem aniversário no mês
informado.
Veja o exemplo para o mês com valor 4 e 50000 para a população:

CIDADES COM MAIS DE 50000 HABITANTES E ANIVERSÁRIO EM ABRIL:
Penedo(AL) tem 59020 habitantes e faz aniversário em 12 de abril.
Itacoatiara(AM) tem 84676 habitantes e faz aniversário em 25 de abril.
Araci(BA) tem 51912 habitantes e faz aniversário em 7 de abril.
Fortaleza(CE) tem 2431415 habitantes e faz aniversário em 13 de abril.
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
    mes = int(input())
    populacao = int(input())
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
    
    res = f"CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {messs}:\n"
    for cidade in cidades:
        if cidade[5] > populacao and cidade[4] == mes:
            if (mes == 1):
                mess = "JANEIRO"
            elif (mes == 2):
                mess = "FEVEREIRO"
            elif (mes == 3):
                mess = "MARÇO"
            elif (mes == 4):
                mess = "ABRIL"
            elif (mes == 5):
                mess = "MAIO"
            elif (mes == 6):
                mess = "JUNHO"
            elif (mes == 7):
                mess = "JULHO"
            elif (mes == 8):
                mess = "AGOSTO"
            elif (mes == 9):
                mess = "SETEMBRO"
            elif (mes == 10):
                return "OUTUBRO"
            elif (mes == 11):
                mess = "NOVEMBRO"
            elif (mes == 12):
                messs = "DEZEMBRO"

            res += f"{cidade[2]}({cidade[0]}) tem {cidade[5]} habitantes e faz aniversário em {cidade[3]} de {mess.lower()}.\n"


    print(res.strip())

if __name__ == "__main__":
    main()
