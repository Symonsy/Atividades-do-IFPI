def analisar(resposta):
    if resposta == "a":
        return "como assim boy"
    elif resposta == "b":
        return ":) acertou"
    elif resposta == "c":
        return "errou"

ask = input("Por que a velhinha não usa relógio?\n"
            "a- porque sim\n"
            "b- porque ela é senhora\n"
            "c- porque ela não precisa\n").lower()
res = analisar(ask)

print(res)