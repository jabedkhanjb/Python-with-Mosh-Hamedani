import random
guess_number = random.randint(1, 9)
#print(guess_number)
i = 0
guess_limit = 3
while i < guess_limit:
    guess = (input("Guess: "))
    i += 1
    if guess == guess_number:
        print("You Won!")
        break
else:
    print("Sorry! you failed.")
    print(f"Your guessing number was {guess_number}")