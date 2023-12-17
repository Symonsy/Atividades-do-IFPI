def quiz(response):
    if response == "chuva":
        return ":) acertou"
    else:
        return " :( vai pesquisar e vê o que é"

ask = str(input("o que é o que é, cai em pé e corre deitado? \n")).lower()
res = quiz(ask)

print(res)