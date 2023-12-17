'''
05. O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha
Maurítius, na costa leste da África. A partir do ano 1600, durante cada ano, 6%
dos animais dos animais vivos no começo do ano morreram e o número de
animais nascidos ao longo do ano que sobreviveram foi de 1% da população
inicial.
Escreva um programa que leia a população de aves no início do ano 1600 e
imprime, anualmente, a partir do fim de 1600, o número de nascimentos, mortes e o total da população
por ano (apenas a parte inteira do números, separados por vírgula). O programa encerra sua execução
quanto a população total cai para menos de 10% da população original.
Bom Trabalho!
'''

def dodo(populacao_inicial):
    ano = 1600
    populacao = populacao_inicial
    nascimentos = 0
    mortes = 0

    while populacao >= 0.1 * populacao_inicial:
        # Calcula o número de nascimentos como 1% da população atual.
        nascimentos = populacao * 0.01

        # Calcula o número de mortes como 6% da população atual.
        mortes = populacao * 0.06

        # Atualiza a população para o próximo ano, considerando nascimentos e mortes.
        populacao = populacao + nascimentos - mortes

        # Imprime o ano, número de nascimentos, número de mortes e a população atual.
        print(f"{ano},{nascimentos:.0f},{mortes:.0f},{populacao:.0f}")

        ano += 1

def main():
    # Recebe a população inicial do usuário.
    populacao_inicial = int(input())
    # Chama a função para realizar o cálculo da população de dodôs.
    dodo(populacao_inicial)

if __name__ == "__main__":
    main()
