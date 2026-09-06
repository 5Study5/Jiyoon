# 경우의 수
# 1 / 2

# 1 -> 1 => 1개
# 2 -> 1 1, 2 => 2개
# 3 -> 1 1 1, 1 2, 2 1 => 3개
# 4 -> 1 1 1 1, 1 1 2, 1 2 1, 2 1 1, 2 2 => 5개
# 5 -> 1 1 1 1 1, 1 1 1 2, 1 1 2 1, 1 2 1 1, 2 1 1 1, 1 2 2, 2 1 2, 2 2 1 => 8개

# DP 풀이
# n번째 위치로 직전 위치에서 올 수 있는 경우 = n-1번째 위치에서 1칸 이동 + n-2번째 위치에서 2칸 이동
# 두 경우가 마지막이 1 / 2 =>  안 겹치므로 더할 수 있음
def solution(n):
    
    dp = [0] * (n+1)
    
    dp[0] = 1
    dp[1] = 1
    # dp[2] = 2  # n=1 인 경우, dp[2] 는 없음
    
    for i in range(2, n+1):
        dp[i] = ( dp[i-1] + dp[i-2] )% 1234567
    
    return dp[n] 




# 조합 풀이
# from math import comb

# def solution(n):
#     two = 0       # 2 개수
#     answer = 0
    
#     for two in range(n//2 + 1):
#         one = n- 2*two
#         total = one + two   # 1의 개수 + 2의 개수
        
#         answer += comb(total, two) #전체에서 2개 들어갈 위치 two개 고름
    
#     return answer % 1234567