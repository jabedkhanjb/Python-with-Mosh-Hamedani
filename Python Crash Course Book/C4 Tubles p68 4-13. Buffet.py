food = ("beef", "mutton", "chicken", "burger", "salmon fish")
print("Items in this buffet offers: ")
for buffet in food:
    print(f"> {buffet}")
food = ("Dosa", "Shawarma") #new items added
print("New items added") # a, b ,f, n, r, t, v
for new in food:
    if new not in buffet:
        buffet = new
    print(f"> {buffet}")