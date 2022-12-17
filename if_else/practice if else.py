a = input("Enter a number: ")
print(a, "is saved on 'a'")

b = input("Enter another number: ")
print(b, "is saved on 'b'")

if a > b: print(a, "is greater than ", b)
elif a < b:
    print(a, "is less than ", b)
else:
    print(a, "and", b , "is equal")