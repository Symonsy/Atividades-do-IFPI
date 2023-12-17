'''4. Um time de basquete possui 12 jogadores. Deseja-se um programa que, dado o nome e a altura
dos jogadores, determine:
a. o nome e a altura do jogador mais alto;
b. a média de altura do time;
c. os jogadores com altura superior à média, listando o nome e a altura de cada um.'''


def lA(n, h):
    
    tallestplayer = max(h)
    ind_name = h.index(tallestplayer)
    name = n[ind_name]
    return f'JOGADOR MAIS ALTO DO TIME\n{name}\n{tallestplayer:.2f}'

def lB(h):
    
    m = sum(h) / len(h)
    return f'ALTURA MÉDIA DO TIME\n{m:.2f}'


def lC(n, h):
    tallest_players = []
    average = sum(h) / len(h)

    for i in range(len(h)):
        if h[i] > average:
            tallest_players.append(n[i])
            tallest_players.append(h[i])

    result = ("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME\n")
    for i in range(0, len(tallest_players), 2):
        result += f"{tallest_players[i]}\n{tallest_players[i + 1]:.2f}\n"

    return (result).strip()

def main():
    list_of_players = []
    height_of_players = []
    
    for i in range(12):
        player = str(input())
        list_of_players.append(player)
        height = float(input())
        height_of_players.append(height)
    
    res_A = lA(list_of_players, height_of_players)
    res_B = lB(height_of_players)
    res_C = lC(list_of_players, height_of_players)

    print(f'{res_A}\n{res_B}\n{res_C}')

if __name__ == "__main__":
    main()
