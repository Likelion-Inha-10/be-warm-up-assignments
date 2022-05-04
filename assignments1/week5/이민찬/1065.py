num = int(input())

hs = 0

for n in range(1, num+1):
    if n <= 99:
        hs += 1
    else:
        nums = list(map(int, str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2] :
            hs += 1

print(hs)