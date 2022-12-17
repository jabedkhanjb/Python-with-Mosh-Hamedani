#Logic AND gate
a = input("Insert a number: ")
b = input("Insert another number: ")
c = input("Insert one more number: ")

print("1st number:", a, "2nd number:", b, "3rd number:", c)

if a > b and a > c:
    print("a:", a, "is the largest number.")
elif b > a and b > c:
    print("b:", b, "is the largest number.")
elif c > a and c > b:
    print("c:", c, "is the largest number.")
else:print("Something went wrong.\nYou have inserted the same value on each variable.")