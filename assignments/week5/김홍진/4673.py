def self_num(n):
    num=n
    while True:
        if n>=10:
            num+=n%10
            n=n/10
            
        else:
            num+=n
            break
        
    return num

num_list=[]

for i in range(10000):
    num_list.append(self_num(i))
    

ans=list(set(range(10000))-set(num_list))
ans.sort()

for ans in ans:
    print(ans)
        
        
         