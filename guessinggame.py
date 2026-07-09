import random
random.randint(1,1000)

jackpot=random.randint(1,1000)
guess=int(input("guess number:"))
counter=1

while guess!=jackpot:
    if guess<jackpot:
        print("guess higher")
    else:
        print("guess lower")

    guess=int(input("guess number:"))
    counter+=1

print("right guess")
print("you tool",counter,"attempts")


