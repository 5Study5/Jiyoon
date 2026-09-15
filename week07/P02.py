import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]

    # 양방향 그래프 만들기
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    INF = float('inf')
    distance = [INF] * (N + 1)

    # 1번 마을 시작
    distance[1] = 0

    heap = []
    heapq.heappush(heap, (0, 1))   # (거리, 마을번호)

    while heap:
        dist, now = heapq.heappop(heap)

        # 이미 더 짧은 거리로 방문한 적 있으면 무시
        if dist > distance[now]:
            continue

        for next_node, cost in graph[now]:
            new_dist = dist + cost

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    answer = 0

    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1

    return answer