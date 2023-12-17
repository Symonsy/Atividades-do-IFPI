'''

preço = int(input('preço: '))
v_p = int(input('percentual: '))

percentual = v_p/100* preço

v_au = int(preço + percentual)
v_di = int(preço - percentual)

print(f'{v_au}, {v_di}')

'''


def precinho(preço, v_p):
    percentual = preço * v_p/100
    global v_au
    global v_di
    v_au = float(preço + percentual)
    v_di = float(preço - percentual)

    return v_au, v_di


def main():

    preç = float(input())
    valor_percentual = float(input())

    precinho(preç, valor_percentual)

    print(f'{v_au:.2f}\n{v_di:.2f}')

if __name__ == "__main__":
    main()








'''def vals(valor, porentagem):
    va1 = valor + (porentagem/100*valor)
    va2 = valor - (porentagem/100*valor)
    m = va1, va2

    return m


valo_r = float(input())
po_rcentagem = float(input())
m = vals(valo_r, po_rcentagem)
print(f'{m:.2f}')
'''