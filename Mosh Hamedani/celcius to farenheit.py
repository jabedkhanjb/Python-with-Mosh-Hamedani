weather = float(input("Insert today's temperature: "))
c_or_f = input("Did you input the value of Celcius or Fahrenheit?\nEnter the name of it.\n")
if c_or_f.upper() == "Celcius":
    c_to_f = ((weather - 32) / 9) * 5
    print(f"Temparature is {c_to_f} degree farenheit")
else:
    f_to_c = ((weather * 5) - 32 * 5) / 9
    print(f"Temparature is {f_to_c} degree celcius")
