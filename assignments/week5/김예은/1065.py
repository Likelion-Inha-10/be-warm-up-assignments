
N = int(input())

H = 0 # 한수의 수
count = 1

while (count <= N):
    if(count < 100): # ~99
        count += 1
        H += 1

    else: # 100~999
        N_list = list(map(int,str(count)))
        if (N_list[0] - N_list[1] == N_list[1] - N_list[2]):
            count += 1
            H += 1
        else:
            count += 1

print(H)
