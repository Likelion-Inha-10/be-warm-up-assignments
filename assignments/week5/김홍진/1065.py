num=int(input())


if num<100:
    print(num)
    101
else:
    i=99
    for a in range(100,num+1):
        k=str(a)
        if int(k[0])-int(k[1]) == int(k[1])-int(k[2]):
            i=i+1

print(i)    