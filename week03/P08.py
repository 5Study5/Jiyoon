#엥 뭐라노..

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    # 좌표가 최대 50인데 2배할 것이므로 넉넉하게 102
    board = [[0] * 102 for _ in range(102)]
    
    # 1. 직사각형들을 2배해서 채우기
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1
    
    # 2. 직사각형 내부를 0으로 만들기
    # → 테두리만 1로 남긴다
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0
    
    # 시작점 / 도착점도 2배
    startX = characterX * 2
    startY = characterY * 2
    
    targetX = itemX * 2
    targetY = itemY * 2
    
    queue = deque()
    queue.append((startX, startY, 0))
    
    visited = [[False] * 102 for _ in range(102)]
    visited[startX][startY] = True
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 아이템 위치에 도착
        if x == targetX and y == targetY:
            return dist // 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 테두리가 아니면 이동 불가
            if board[nx][ny] == 0:
                continue
            
            # 이미 방문한 곳
            if visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            queue.append((nx, ny, dist + 1))