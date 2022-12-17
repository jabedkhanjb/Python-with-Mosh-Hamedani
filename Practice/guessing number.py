print("*" * 40)
print("      Guessing number Practice code")
print("*" * 40)

import random
secret_number = random.randint(1, 9) #randrange can be used
countdown = 0
guess_limit = 3
#print(secret_number) # here we can see the random number which has been taken from computer
while countdown < guess_limit:
    guess = int(input("Guess: "))
    if guess < secret_number:
        print("Higher...")
    elif guess > secret_number:
        print("Lower...")
    countdown += 1

    if guess == secret_number:
        print(f"Congratulations, you won! your secret number was {secret_number}")
        print(f"And it only took you {countdown} tries")
        break
    if countdown == guess_limit:
        print(f"Sorry, you failed!\nYour secret number was {secret_number}")