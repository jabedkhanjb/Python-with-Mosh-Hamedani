thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(f"Here the number of items are {len(thistuple)}")

thistuple = ("apple",)
print(type(thistuple))

# #NOT a tuple
thistuple = ("apple")
print(type(thistuple))

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

item = tuple(("apple", "banana", "mango"))
print(item)
print(type(item))

thistuple = ("apple", "banana", "cherry", "strawberry")
print(thistuple[3])
thistuple = ("apple", "banana", "cherry")
print(thistuple[-3])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1:])

thistuple = ("apple", "banana", "cherry")
newitem = "strawberry"
thistuple = newitem
if newitem in thistuple:
    print(f"Yes, {newitem} is in the fruits tuple")
else:
    print(f"Sorry, {newitem} is not included in this tuple")

fruit = ("apple", "banana", "mango")
newitem = list(fruit)
newitem.append("orange")
newitem.insert(1, "orange")
newitem.remove("banana")
fruit = tuple(newitem)
print(type(fruit))
print(fruit)

thistuple = ("apple", "banana", "cherry")
#del thistuple
print(thistuple)

fruits = ("apple", "banana", "cherry")
print(fruits.count("banana"))
print(fruits)
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)