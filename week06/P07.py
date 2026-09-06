def solution(N, number):
    
    # N 사용횟수 최솟값이 8보다 크면 -1 반환. 즉, 8까지만 검사
    dp = [set() for _ in range(9)]

    for i in range(1, 9):

        # N, NN, NNN, ...
        dp[i].add(int(str(N) * i))

        for j in range(1, i):

            for a in dp[j]:
                for b in dp[i-j]:

                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)

                    if b != 0:
                        dp[i].add(a // b)

        if number in dp[i]:
            return i

    return -1