for x in [0, 1, 2, 3, 4, 5]:
    pass
    print("Program passed")
print("*" * 20)

n, m, a = map(int, input().split())

if m % a == 0:
    r1 = m // a
else:
    r1 = m // a + 1

if n % a == 0:
    r2 = n // a
else:
    r2 = n // a + 1

print(r1 * r2)