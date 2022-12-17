random = [10, 12, 14, 10, 9, 8, 14, 8, 16, 15, 21, 19, 16]
print(f"There are a bunch of duplicate numbers included in this list has given below.\n{random}")
unique = []
print(unique)
for number in random:
    print("Here are the first number is", number)
    if number not in unique:
        print(number, "is not in", unique)
        unique.append(number) #append = connect, so here we connect all the item in unique from number.
        print("We are saving the number:", unique)
    else:
        print(number, "is already taken. we don't allow duplicate numbers.")
print(f"So we got all unique numbers which are {unique}")
unique.sort()
print(f"Now we gonna sort it in a sequence as below: \n{unique}")
print("""
\nCoded by @jabedkhanjb
visit me: https://allmylinks.com/jabedkhanjb
""")

print("Without instruction: ")
random = [10, 12, 14, 10, 9, 8, 14, 8, 16, 15, 21, 19, 16]
print(f"There are a bunch of duplicate numbers included in this list has given below.\n{random}")
unique = []
for number in random:
    if number not in unique:
        unique.append(number)
print(unique)