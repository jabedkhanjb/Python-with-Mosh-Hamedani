phone = input("Enter number: ")
digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}
output = ""
print(phone)
for character in phone:
    output = output + digit_mapping.get(character, "<invalid>") + " "
print(output)