# BFS

from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    # 각 칸까지의 거리(칸 개수) 저장, 0으로 초기화
    distance = [[0] * m for _ in range(n)]
    
    queue = deque() # 양방향 큐(double ended queue)
    queue.append((0, 0)) # 시작점 인덱스
    
    distance[0][0] = 1  # 시작점 칸 개수 1개
    
    # (dr,dc) => 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:  # 큐가 비어있지 않을 때까지(True) 반복
        row, col = queue.popleft() # 왼쪽(= 먼저 들어온 데이터)부터 꺼냄

        for i in range(4): # 상/하/좌/우 확인
            next_row = row + dr[i]
            next_col = col + dc[i]

            # 맵 밖이면 무시
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= m:
                continue

            # 벽이면 무시
            if maps[next_row][next_col] == 0:
                continue

            # 이미 방문한 곳이면 무시
            if distance[next_row][next_col] != 0:
                continue

            distance[next_row][next_col] = distance[row][col] + 1
            queue.append((next_row, next_col))

    # 도착할 방법 없는 경우, -1 리턴
    if distance[n - 1][m - 1] == 0:
        return -1

    return distance[n - 1][m - 1]
