weather = float(input("Insert today's temperature: "))
temperature = input("Did you input the value of Celsius or Fahrenheit?\nEnter the name of it: ")

if temperature == "Celsius" or "celsius" or "c":
    C_to_F = ((weather - 32) / 9) * 5
    print(f"Temperature is {C_to_F} degree fahrenheit")

elif temperature == "Fahrenheit" or "fahrenheit" or "f":
    F_to_C = ((weather * 5) - 32 * 5) / 9
    print(f"Temperature is {F_to_C} degree celsius")

else:
    print("Something went wrong.")
print("\nVisit https://allmylinks.com/jabedkhanjb\nLike, Share and subscribe")