num1 = set(range(1,10001))
num2 = set()

for n in range(1, 10001):
    for m in str(n):
        n += int(m)
    num2.add(n)

num = sorted(num1 - num2)
for n in num:
    print(n)
