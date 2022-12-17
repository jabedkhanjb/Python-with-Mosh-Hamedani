#task
# price of a house is $1M
# if buyer has good credit
#   they need to put down 10%
# otherwise
#   they need to put down 20%
# print the down payment
# solution
print("*" * 20)
price = 1000000
has_good_credit = False
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")
print("*" * 20)
#sequentially

a = input("Set number for a: ")
b = input("Set number for b: ")
if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
print('*' * 20)

c = input('enter a number: ')
d = input('enter another number: ')
if c > d: print(c, 'is greater than', d)
elif c < d: print(d, 'is greater than', c)
else: print(c, 'is equal to', d)
print('*' * 20)

one = input('Number: ')
two = input('Another Number: ')
print("Jabed") if one > two else print("Mahfuz")
print('*' * 20)

A = input("Set a number for A: ")
B = input("Set a number for B: ")
print("A is large") if A > B else print("=") if A == B else print("B is large")

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