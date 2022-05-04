"""
def fibonacci(n):
    if(n==0):
        print("0")
        return 0
    elif(n==1):
        print("1")
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
"""
def fib(n):
 
 T=input()
 for i in range(T):
    N=input()
    zero=[1,0,1]
    one=[0,1,1]
    for i in range(3,N+1):
        zero.append(zero[i-1]+zero[i-2])
        one.append(one[i-1]+one[i-2])
    print(zero[N],one[N])
