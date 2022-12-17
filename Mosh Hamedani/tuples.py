food = ("beef", "mutton", "chicken", "burger", "salmon fish")
print("Items in this buffet offers: ")
for buffet in food:
    print(f"> {buffet}")
print(len(food))
food = ("Dosa", "Shawarma") #new items added
print("New items added") # a, b ,f, n, r, t, v
for new in food:
    if new not in buffet:
        buffet = new
    print(f"> {buffet}")
print(len(food))
tuple = ("item",)
print(type(tuple), tuple)
tuple = ("item")
print(type(tuple), tuple)
food = ("beef", "mutton", "chicken", "burger", "salmon fish")
print(food[1:4])

thistuple = ("apple", "banana", "cherry")
item = "sausage"
if item in thistuple:
  print(f"Yes, {item} is in the fruits tuple")
else:
    print(f"There is no {item} over in this tuple.")

fruit = ("apple", "banana", "mango")
newitem = list(fruit)
print(type(newitem))
newitem[1] = "cherry"
fruit = newitem
print(fruit)


