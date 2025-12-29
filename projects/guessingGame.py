import random

secretNum = random.randint(0, 100)

guessCount = 0
guessLimit = 3
while guessCount < guessLimit: 
    guess = int(input('Guess: ' ))
    guessCount += 1
    if guess == secretNum:  
        print("You won!")
        break
else: 
    print("You failed")