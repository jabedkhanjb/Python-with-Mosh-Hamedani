#logic gate
first = input("Enter first number: ")
sec = input("Enter sec number: ")
last = input("Enter last number: ")
if first > sec and first > last:
    print(first, "is the largest number")
elif sec > first and sec > last:
    print(sec, "is the largest number")
elif last > first and last > sec:
    print(last, "is the largest number")
else:
    print("Something error")