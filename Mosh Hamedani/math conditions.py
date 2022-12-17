price = 10000
good_credits = False

if good_credits:
    down_payment = price * 0.1
else:
    down_payment = price * 0.3
print(f"Down Payment: ${down_payment}")

total = price - down_payment
print(f"You have to pay ${total}")