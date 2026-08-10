def solution(n, computers):
    
    answer = 0
    visited = [False] * n

    def dfs(current):
        visited[current] = True

        for next_computer in range(n):
            if computers[current][next_computer] == 1 and not visited[next_computer]:
                dfs(next_computer)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer