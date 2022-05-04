num = str(input())

def check(num):
    if len(num) <= 2:
        return int(num)
    p = 0
    q = len(num) - 1
    while p != q:
        x = int(num[p])
        y = int(num[q])
        p += 1
        q -= 1
        if x - int(num[p]) != int(num[q])-y:
            return int(0)
    return int(1)

i = 0
if len(num)<=2:
    i += check(num)
else:
    while int(num)>=99:
        i += check(num)
        num=str(int(num)-1)

print(i)