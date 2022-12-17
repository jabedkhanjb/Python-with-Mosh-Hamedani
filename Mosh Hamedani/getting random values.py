import random

for i in range(3):
    print(random.randint(15, 30))

member = ["Renu", "Kona", "Jabed"]
pick = random.choice(member)
print(f"Congratulations {pick}")

print("\nHere we are using something exceptional\n")


class Dice:

    def roll(self):
        fnumber = random.randint(1, 6)
        lnumber = random.randint(1, 6)
        return fnumber, lnumber


newdice = Dice()
print(newdice.roll())