weight = input("Weight: ")
converter = input("(L)bs or (K)g\n:")
if converter.upper() == "L":
    kilos = int(weight) * 0.45
    print(f"You are {kilos} kilos.")
elif converter.upper() == "K":
    lbs = int(weight) / 0.45
    print(f"You are {lbs} pounds")
else:
    print("Something went wrong")
print("\nPython Programming,\nConducted by jabedkhanjb.\nSupport Team")
