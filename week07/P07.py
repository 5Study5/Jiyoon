from collections import deque

def solution(board):
    rows = len(board)
    cols = len(board[0])

    # 시작 위치 찾기
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'R':
                start = (r, c)

    visited = [[False] * cols for _ in range(rows)]

    queue = deque()
    queue.append((start[0], start[1], 0))

    visited[start[0]][start[1]] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c, count = queue.popleft()

        if board[r][c] == 'G':
            return count

        for i in range(4):
            nr = r
            nc = c

            # 해당 방향으로 끝까지 이동
            while True:
                next_r = nr + dr[i]
                next_c = nc + dc[i]

                # 다음 칸이 보드 밖이면 멈춤
                if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
                    break

                # 다음 칸이 장애물이면 멈춤
                if board[next_r][next_c] == 'D':
                    break

                nr = next_r
                nc = next_c

            # 새로 도착한 위치를 아직 방문 안 했다면
            if not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, count + 1))

    return -1