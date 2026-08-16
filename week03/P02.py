def solution(k, dungeons):
    answer = -1
    
    visited = [False] * len(dungeons)

    # 재귀 dfs
    def dfs(fatigue, count):
        nonlocal answer

        answer = max(answer, count)

        for i in range(len(dungeons)):
            if not visited[i] and fatigue >= dungeons[i][0]:
                visited[i] = True

                dfs(
                    fatigue - dungeons[i][1],
                    count + 1
                )

                visited[i] = False

    dfs(k, 0)

    return answer