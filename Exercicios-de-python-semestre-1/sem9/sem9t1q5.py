'''
Escreva um programa que leia um número inteiro e calcule o resto da divisão inteira do número lido por 5 (cinco). 
A seguir, de acordo com o resultado da divisão, faça o que é solicitado abaixo:

Se 0 (zero), escreva a o resultado da equação 9n + 7, onde n é o valor lido;
Se 1 (um), escreva se o valor lido é par ou ímpar;
Se 2 (dois), escreva a o resultado da equação 5n2 – 3n + 42, onde n é o valor lido;
Se 3 (três), escreva a divisão inteira do valor lido por 10;
Se 4 (quatro), escreva o quadrado do valor lido;
'''


def ver(valor):

    if valor == 0:
        return (9 * 0 + 7)
    
    resto = valor % 5

    if resto == 0:
        return (9 * valor + 7)
    if resto == 1:
        if valor % 2 == 1:
            return 'ímpar'
        else:
            return 'par'
    if resto == 2:
        return (5 * valor**2 - 3 * valor + 42)
    if resto == 3:
        return (valor // 10)
    if resto == 4:
        return (valor**2)


numero = int(input())
result = ver(numero)

print(result)