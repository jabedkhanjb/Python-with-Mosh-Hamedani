#access tuples

fruit = ("apple", "mango", "banana")
newitem = list(fruit) #tuple is immutable, so we have to convert it into a list,
                        # so that we can be able to add new items
newitem[2] = "cherry"
fruit = tuple(newitem)
print(type(fruit), f"\nAccessed successfully in the tuple.\nItems are {fruit} ")
print("\n")
#adding items using append in tuple
#update tuples
food = ("fish", "rice", "egg")
newfood = list(food)
newfood.append("chicken") #newfood.insert(0, "chicken")
food = tuple(newfood)
print("We have successfully added a new item using append in tuple by converting it into a list.\n", food)

#creating new tuple
x = ("car", "plane", "train", "bike")
y = ("bus",) #when you're adding a only one item in tuple, don't forget to use comma<,> afterwards the ending quotation.

x += y
print(x)

#remove item from tuple converting it into list
tupleitem = ("car", "plane", "train", "bike", "bus")
removeitem = list(tupleitem)
removeitem.remove("bike")
tupleitem = tuple(removeitem)
print(tupleitem)

#del / delete tuple completely
print("Here is our tuple items: ", tupleitem)
del tupleitem
print(f"we've used <del> command to delete tuple items: {tupleitem}")
