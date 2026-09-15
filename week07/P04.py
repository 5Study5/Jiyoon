from collections import deque

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]

    # 양방향 그래프 만들기
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # destination에서 각 지역까지의 최단거리
    distance = [-1] * (n + 1)
    distance[destination] = 0

    queue = deque([destination])

    while queue:
        now = queue.popleft()

        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                queue.append(next_node)

    answer = []

    for s in sources:
        answer.append(distance[s])

    return answer