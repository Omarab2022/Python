import random

choises=["rock",'paper','scissors']

computer = random.choice(choises)

player = None
while player not in choises:
 player = input("rock,paper or scissors ? ").lower()


print("computer : " + computer)
print("player : " + player)

if computer=="rock" and player=="paper" :
    print(" you win !!!!")
elif computer=="paper" and player=="scissors" :
    print(" you win!!!!")
elif computer=="scissors" and player==  "rock" :
    print(" you win!!!!")
elif computer == player :
    print(" you tie!!!!")
else :
    print(" you lose!!!!")