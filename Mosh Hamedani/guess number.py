print("*" * 40)
print("          Guessing number game")
print("*" * 40)
import random

secret_number = random.randint(1, 9) #int(input("Insert a secret number: "))
guess_count = 0
guess_limit = 3
print(secret_number)
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print(f"Sorry, you failed!\nYour random number was {secret_number}")
print()
print("*" * 40)
print("Coded by @jabedkhanjb\nhttps://allmylink.com/jabedkhanjb")