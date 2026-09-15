from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]

    # 양방향 그래프 만들기
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n + 1)
    distance[1] = 0

    queue = deque([1])

    while queue:
        now = queue.popleft()

        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                queue.append(next_node)

    max_dist = max(distance)

    return distance.count(max_dist)