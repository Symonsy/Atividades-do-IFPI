def quiz(response1, response2, response3):

    score = 0

    if response1 == "requeijão":
        score +=1
    if response2 == "suvacuo":
        score +=1
    if response3 == "chuva":
        score+=1
    return f'{score}, obg por jogar!'

ask1 = str(input("Qual é o rei dos queijos? \n")).lower()
ask2 = str(input("Qual parte do corpo não tem ar? \n")).lower()
ask3 = str(input("o que é o que é, cai em pé e corre deitado? \n")).lower()

res = quiz(ask1, ask2, ask3)
print(res)