# A função 'eh_vogal' é criada com o parâmetro 'caractere' que é definido pela variável 'caractere' que recebe a letra a ser verificada se é vogal.


def eh_vogal(caractere):
    if caractere != 'a' and caractere != 'e' and caractere != 'i' and caractere != 'o' and caractere != 'u':
        return False
    else:
        return True


caractere = input('digite uma letra': )
print(eh_vogal(caractere))
