print("*" * 40)
print("          Guessing Number Game\n      Guess a number between 1 to 9")
print("*" * 40)
import random
secret_number = random.randint(1, 9)
tries = 0
guessing_limit = 3
#print(secret_number)
while tries < guessing_limit:
    guess = int(input("Guess: "))
    if guess < secret_number:
        print("Higher...")
    elif guess > secret_number:
        print("Lower...")
    tries += 1

    if guess == secret_number:
        print(f"Congratulations, you won! Your secret number is {secret_number}")
        print(f"And it only took you {tries} tries.")
        break
    if tries == guessing_limit:
        print(f"Sorry, you failed.\nYour secret number was {secret_number}")
print("\nLike, share and subscribe my channel.\nvisit: https://allmylinks.com/jabedkhanjb")