nums = [i for i in range(1,10001)]
for i in range(1,10000):
    dn=i
    for j in str(i):
        dn+=int(j)
        if dn>10000:
            break
    if dn<=10000 and dn in nums:
        nums.remove(dn)

for i in nums:
    print(i)