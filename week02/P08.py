from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append((begin, 0))

    visited = [False] * len(words)

    while queue:
        current, count = queue.popleft()

        if current == target:
            return count

        for i in range(len(words)):
            if visited[i]:
                continue

            diff = 0

            for j in range(len(current)):
                if current[j] != words[i][j]:
                    diff += 1

            if diff == 1:
                visited[i] = True
                queue.append((words[i], count + 1))

    return 0