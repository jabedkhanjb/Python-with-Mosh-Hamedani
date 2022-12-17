temperature = input("Insert the temperature: ")

if float(temperature) >= 30:
    print("This is a hot weather today.")
elif float(temperature) <= 10:
    print("This is a cold weather today.")
else:
    print("It's neither hot or cold")