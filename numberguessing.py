import random

# Generate the random jackpot number
jackpot = random.randint(1, 1000)
guess = int(input("guess number:"))
counter=1

while guess!=jackpot:
    if guess<jackpot:
        print("guess higher")
    else:
        print("guess lower")
    
    # Force the program to wait for new input
    guess=int(input("guess again:"))
    counter+= 1

print("right guess")
print("you took",counter,"attempts")