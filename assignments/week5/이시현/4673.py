nums = []
def constructor():
    for i in range (1,10001,1):
        k=0
        if(i>=1000):
            k = i + int(i/1000) + int((i%1000)/100) +int((i%100)/10) + i%10  # 각 자릿수 추출해서 더하기
            if(k<=10000):
                nums.append(k) # 합이 10000 이하일 때 nums 리스트에 추가
            
        elif(i>=100):
            k = i + int(i/100) + int((i%100)/10) + i%10
            nums.append(k)

        elif(i>=10):
            k = i + int(i/10)+ (i%10)
            nums.append(k)

        elif(i>0):
            k = i+i
            nums.append(k)

        else:
            continue

nums_10000 = range(1,10001) # 1~10000 까지의 모든 수가 저장된 리스트
constructor()
selfnum = set(nums_10000) - set(nums) # 차집합
for k in sorted(selfnum): # 오름차순으로 정렬 후 출력
    print(k)




    




            
            

