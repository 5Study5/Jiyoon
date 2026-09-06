def solution(n):
    
    dp = [0] * (n+1)     # [0,n] => n+1 개
    
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = (dp[i-1]+dp[i-2]) %1234567

    return dp[n]




# run time error
# def solution(n):
#     return fibo(n)%1234567

# def fibo(k):
    
#     if (k==0):
#         return 0
#     elif (k==1):
#         return 1
#     else:
#         return fibo(k-1)+fibo(k-2)