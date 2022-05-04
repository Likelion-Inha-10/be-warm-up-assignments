# !!이 문제는 어려워서 구글링 곁들여 풀었습니다!! 혼자 힘으로 푼 것 NONO


# def fibonacci(n):
#     if(n == -1):  # 입력값이 0 일 때
#         return 0
#     elif(n==0): # 입력값이 1 일 때
#         return 1
#     else:
#         first = 0
#         second = 1
#         sum = first + second

#         while (n > 0):
#             sum = first + second
#             first =second
#             second =sum
#             n -= 1
#         return sum

# times = int(input())
# for i in range(times):
#     n = int(input())-1
#     print(fibonacci(n-1), fibonacci(n))
