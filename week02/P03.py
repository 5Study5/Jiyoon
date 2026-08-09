from collections import deque

def solution(maps):
    answer = []
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for row in range(n):
        for col in range(m):

            # 바다이거나 이미 방문한 곳이면 건너뜀
            if maps[row][col] == 'X' or visited[row][col]:
                continue

            queue = deque()
            queue.append((row, col))
            visited[row][col] = True

            food = 0

            while queue:
                r, c = queue.popleft()

                food += int(maps[r][c])

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    # 맵 밖이면 무시
                    if nr < 0 or nr >= n or nc < 0 or nc >= m:
                        continue

                    # 바다면 무시
                    if maps[nr][nc] == 'X':
                        continue

                    # 이미 방문했다면 무시
                    if visited[nr][nc]:
                        continue

                    visited[nr][nc] = True
                    queue.append((nr, nc))

            answer.append(food)

    if len(answer) == 0:
        return [-1]

    answer.sort()

    return answer