#Logic OR gate
a = input("Enter number: ")
b = input("Enter number: ")
c = input("Enter number: ")

print("a = ", a, "b = ", b, "c = ", c)

if a > b or a > c:
    print(a, "is larger.")
if b > a or b > c:
    print(b, "is larger.")
elif c > a or c > b:
    print(c, "is larger.")