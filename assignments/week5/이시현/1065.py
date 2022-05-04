

def hansu(k):
    num = 0

    if(k>=100):
        num = 99


        for t in range(100,k+1,1):
            hrd = int(t/100)            # 백의 자리
            ten = int((t-hrd*100)/10)   # 십의 자리
            one = int(t-int(t/10)*10)   # 일의 자리
            if((hrd-ten)==(ten-one)):   # 공차 확인
                num += 1

    else:
        num = k
    
    return num



t = input()
print(hansu(int(t)))