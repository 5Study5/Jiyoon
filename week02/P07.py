from collections import deque

def solution(places):
    answer = []
    
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer


def check(place):
    for row in range(5):
        for col in range(5):

            if place[row][col] == 'P':
                if not bfs(place, row, col):
                    return False

    return True


def bfs(place, start_row, start_col):
    queue = deque()
    queue.append((start_row, start_col, 0))

    visited = [[False] * 5 for _ in range(5)]
    visited[start_row][start_col] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        row, col, dist = queue.popleft()

        # 거리가 2면 더 멀리 갈 필요 없음
        if dist == 2:
            continue

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            # 대기실 밖
            if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
                continue

            # 이미 확인한 곳
            if visited[nr][nc]:
                continue

            # 파티션은 통과 불가능
            if place[nr][nc] == 'X':
                continue

            # 거리 2 이내에 다른 사람이 있으면 거리두기 위반
            if place[nr][nc] == 'P':
                return False

            # 빈 자리라면 계속 탐색
            visited[nr][nc] = True
            queue.append((nr, nc, dist + 1))

    return True