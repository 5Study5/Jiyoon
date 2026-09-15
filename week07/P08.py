def solution(n, s, a, b, fares):
    INF = 10**15

    # 거리 배열
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신까지 거리는 0
    for i in range(1, n + 1):
        dist[i][i] = 0

    # 양방향 요금 저장
    for x, y, cost in fares:
        dist[x][y] = cost
        dist[y][x] = cost

    # 플로이드-워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    answer = INF

    # k번 지점에서 갈라진다고 가정
    for k in range(1, n + 1):
        cost = dist[s][k] + dist[k][a] + dist[k][b]
        answer = min(answer, cost)

    return answer