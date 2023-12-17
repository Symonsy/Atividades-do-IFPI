


def dodo(populacao_inicial):
    ano = 1601
    populacao = populacao_inicial
    nascimentos = 0
    mortes = 0

    while populacao >= 0.1 * populacao_inicial:
        nascimentos = int(populacao * 0.01)
        mortes = int(populacao * 0.06)
        populacao = populacao - mortes + nascimentos

        print(f"{ano},{nascimentos},{mortes},{populacao}")
        ano += 1

def main():
    populacao_inicial = int(input())
    dodo(populacao_inicial)

if __name__ == "__main__":
    main()
