country = input("Which country you're going > ")
split_country = country.split()
without_redundancy = {
    "usa": "USA",
    "Usa": "USA",
    "USA": "USA",
    "America": "USA",
    "america": "USA",
}
removed_redundancy = ""
for abroad in split_country:
    removed_redundancy = removed_redundancy + without_redundancy.get(abroad, abroad) + " "
print(removed_redundancy)



text = input("Enter your text: \n> ")
breaking = text.split(" ")
emoji = {
    "1": "Jabed",
    ":)": "🙂",
    ":(": "😔",
    ":/": "😒",
    "-_-": "😑",
    "*_*": "😍"
}
final = ""
for new in breaking:
    final = final + emoji.get(new, new) + " "
print(final)