from collections import deque

def solution(n, wires):
    answer = n

    for cut in range(len(wires)):
        graph = [[] for _ in range(n + 1)]

        # cut 번째 전선만 제외하고 그래프 만들기
        for i in range(len(wires)):
            if i == cut:
                continue

            a, b = wires[i]
            graph[a].append(b)
            graph[b].append(a)

        # 한쪽 네트워크의 송전탑 개수 세기
        visited = [False] * (n + 1)

        queue = deque([1])
        visited[1] = True

        count = 1

        while queue:
            current = queue.popleft()

            for next_node in graph[current]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    count += 1

        other = n - count

        difference = abs(count - other)

        answer = min(answer, difference)

    return answer