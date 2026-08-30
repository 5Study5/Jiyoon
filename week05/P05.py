# DP
# dp[x] = x원을 만드는 방법의 수

def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1          # 0원을 만드는 방법의 수: 1개 (아무 동전 사용X)

    for coin in money:
        for price in range(coin, n + 1):
            dp[price] += dp[price - coin]    # dp[5] += dp[3] -> 기존 3원 만드는 방법 뒤에, 2원 coin 하나 붙이면 5원 만들 수 있음.
            dp[price] %= 1000000007

    return dp[n]