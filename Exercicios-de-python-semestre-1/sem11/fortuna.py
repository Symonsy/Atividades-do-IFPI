
from random import *

print('''
Porta da fortuna!
=========

Há um prêmio atrás de uma das 3 portas!
Adivinhe a porta correta para ganhar o prêmio!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|
''')

score = 0

game = True

while game == True:
    
    portaescolhida = int(input())

    portacerta = randint(1,3)

    print("A porta escolhida foi ", portaescolhida)
    print("A porta certa é a ", portacerta)

    if portaescolhida == portacerta:
        score += 1
        print(f"Parabéns!")
    else:
        print("Que peninha!")

    print(f"\nSua pontuação é {score}")

    print("Tentar novamente? (s/n)")
    choice = input()

    if choice == "n":
        game = False
print("Obrigado por jogar.")
print(f"\nSua pontuação final é de {score}")