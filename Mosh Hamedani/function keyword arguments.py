# def greet_user(fname, lname):
#     print(f"Hi {fname} {lname}")
#     print("Welcome to American flight.")
#     print("Departure from Hazrat Shahjalal International Airport, Dhaka")
#     print("Arrival at Minneapolis–Saint Paul International Airport, America")
#
#     greet_user(fname="Jabed,", lname="Mahfuz Islam Khan")
# print("What's your name? ")
# greet_user(input("> ").strip().title(), input("> ").strip().title())

def main():
    x = int(input("What's X? "))
    if is_even(x):
        print(f"{x} is an Even number.")
    else:
        print(f"{x} is an Odd number.")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
