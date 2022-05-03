
def Find(N): # True이면 Self Num 아님
    for i in N_list:
        if (i == N):
            return True
    return False


N_list = []

for i in range(10000):
    if (i < 10): # ~9
        N_list.append(i + i)
    elif (i < 100): # ~99 
        i_list = list(map(int, str(i)))
        N_list.append(i + i_list[0] + i_list[1])
    elif (i < 1000): # ~999
        i_list = list(map(int, str(i)))
        N_list.append(i + i_list[0] + i_list[1] + i_list[2])
    elif (i < 10000): # ~9999
        i_list = list(map(int, str(i)))
        N_list.append(i + i_list[0] + i_list[1] + i_list[2] + i_list[3])
    else: # 10000
        N_list.append(i + i_list[0] + i_list[1] + i_list[2] + i_list[3] + i_list[4])


SN_list = []

for i in range(10000):
    if (Find(i) == False):
        SN_list.append(i)

for i in SN_list:
    print(i)