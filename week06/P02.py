def solution(land):
    dp = land.copy()

    # dp[i][j] : dp[i]행에서, j번째 열 선택했을 경우 최대 점수
    # => land[i-1] 행에서, j 제외한 열의 max 값 더하기
    
    for i in range(1, len(land)):    
        dp[i][0] += max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
        dp[i][1] += max(dp[i-1][0], dp[i-1][2], dp[i-1][3])
        dp[i][2] += max(dp[i-1][0], dp[i-1][1], dp[i-1][3])
        dp[i][3] += max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

    return max(dp[-1])