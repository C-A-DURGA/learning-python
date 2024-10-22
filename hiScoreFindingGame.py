import random


def game():
    print("You're playing a game....")
    score=random.randint(1,100)
    with open("HiScore.txt") as f:
        Hiscore=f.read()
        if (Hiscore!=""):
            Hiscore=int(Hiscore)
        else:
            Hiscore=0
    
    print(f"Your score {score}")
    if(score>Hiscore):
        with open("HiScore.txt","w") as f :
            f.write(str(score))

    return score


game()    