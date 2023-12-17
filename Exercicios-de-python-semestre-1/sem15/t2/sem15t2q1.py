'''01.Faça um programa para ler uma matriz quadrada de ordem n e mostre uma tupla com a posição (linha e coluna) do
maior e menor elemento. O valore de n é inteiro, positivo e deve ser informados pelo usuário'''


def calc(n):
    matriz = []

    for lin in range(n):
        lin = []
        for col in range(n):
            x = int(input())
            lin.append(x)

        matriz.append(lin)

    maior = matriz[0][0]
    menor = matriz[0][0]
    linha_maior = 0
    coluna_maior = 0
    linha_menor = 0
    coluna_menor = 0

    for lin in range(n):
        for col in range(n):
            if matriz[lin][col] > maior:
                maior = matriz[lin][col]
                linha_maior = lin
                coluna_maior = col
            elif matriz[lin][col] < menor:
                menor = matriz[lin][col]
                linha_menor = lin
                coluna_menor = col

    
    tupla_do_maior = (linha_maior, coluna_maior)
    tupla_do_menor = (linha_menor, coluna_menor)

    return f'{tupla_do_maior}\n{tupla_do_menor}'
    
def main():
    
    num = int(input())
    res = calc(num)
    print(res)

if __name__=="__main__":
    main()