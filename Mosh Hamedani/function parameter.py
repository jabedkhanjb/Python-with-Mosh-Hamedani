def greet_user():
    name = input("Enter your name > ")
    country = input("Which country you're going > ")
    split_country = country.split()
    without_redundancy = {
        "usa": "USA",
        "Usa": "USA",
        "USA": "USA",
        "America": "America",
        "america": "America",
    }
    removed_redundancy = ""
    for abroad in split_country:
        removed_redundancy = removed_redundancy + without_redundancy.get(abroad, abroad) + ""

    print(f"Hi {name}")
    if removed_redundancy == "usa" or "America" or "america" or "USA":
        print(f"Welcome to {removed_redundancy}")
    elif country == "uk" or "UK" or "London" or "london":
        print(f"Welcome to {country}")


greet_user()

def defname(new_name):
    print(f"Hi {new_name}")
    print("Welcome abroad")

print("Start")
defname("Jabed")
print("Finish")