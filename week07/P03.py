from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])

    # S, L, E 위치 찾기
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
            elif maps[r][c] == 'E':
                exit_pos = (r, c)

    # S -> L
    dist1 = bfs(maps, start, lever)

    if dist1 == -1:
        return -1

    # L -> E
    dist2 = bfs(maps, lever, exit_pos)

    if dist2 == -1:
        return -1

    return dist1 + dist2


def bfs(maps, start, target):
    rows = len(maps)
    cols = len(maps[0])

    visited = [[False] * cols for _ in range(rows)]

    queue = deque()
    queue.append((start[0], start[1], 0))

    visited[start[0]][start[1]] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c, dist = queue.popleft()

        if (r, c) == target:
            return dist

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위 밖
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue

            # 벽
            if maps[nr][nc] == 'X':
                continue

            # 이미 방문
            if visited[nr][nc]:
                continue

            visited[nr][nc] = True
            queue.append((nr, nc, dist + 1))

    return -1