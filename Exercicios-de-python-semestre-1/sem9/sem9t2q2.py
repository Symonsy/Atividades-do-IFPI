def verificar(num):

    c = num // 100  # Obtém a quantidade de centenas no número
    d = (num % 100) // 10  # Obtém a quantidade de dezenas no número
    u = num % 10  # Obtém a quantidade de unidades no número

    result = ''  # Inicializa uma string vazia para armazenar o resultado

    # Verifica as centenas
    if c > 0:
        if c == 1:
            result += "uma centena"
        else:
            result += ver_u(c) + " centenas"

    # Verifica as dezenas
    if d > 0:
        if result:
            result += ", "  # Adiciona uma vírgula se já houver texto no resultado
        if d == 1:
            result += "uma dezena"
        else:
            result += ver_d(d) + " dezenas"

    # Verifica as unidades
    if u > 0:
        if result:
            if c > 0 or d > 0:
                result += " e "  # Adiciona "e" se já houver centenas ou dezenas no resultado
            else:
                result += ", "  # Caso contrário, adiciona uma vírgula
        if u == 1:
            result += "uma unidade"
        elif u == 2:
            result += "duas unidades"
        else:
            result += ver_u(u) + " unidades"

    return result


def ver_u(num):
    if num == 1:
        return "um"
    elif num == 2:
        return "duas"
    elif num == 3:
        return "três"
    elif num == 4:
        return "quatro"
    elif num == 5:
        return "cinco"
    elif num == 6:
        return "seis"
    elif num == 7:
        return "sete"
    elif num == 8:
        return "oito"
    elif num == 9:
        return "nove"
    else:
        return ""


def ver_d(numero):
    if numero == 1:
        return "uma"
    elif numero == 2:
        return "duas"
    elif numero == 3:
        return "três"
    elif numero == 4:
        return "quatro"
    elif numero == 5:
        return "cinco"
    elif numero == 6:
        return "seis"
    elif numero == 7:
        return "sete"
    elif numero == 8:
        return "oito"
    elif numero == 9:
        return "nove"
    else:
        return ""

def main():
    val = int(input())  # Lê um número inteiro

    res = verificar(val)  # Chama a função verificar para obter o resultado
    print(f'{res}.')  # Imprime o resultado no formato correto

if __name__ == "__main__":
    main()
