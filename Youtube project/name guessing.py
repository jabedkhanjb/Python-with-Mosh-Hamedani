import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 10.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 10)
print("print the random number", the_number)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries += 1
    if tries == 3:
        print("You failed to guess in time!")
        break
    if guess == the_number:
        print("You guessed it! The number was", the_number)
        print("And it only took you", tries, "tries!\n")