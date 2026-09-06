def solution(n):
    answer = 0
    
    # 1 / 2 더해서 n 만들기
    dp = [0] * (n+1)
    dp[0] = 1  # dp[2] = 2
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 1000000007
    
    return dp[n]