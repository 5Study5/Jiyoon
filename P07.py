def solution(tickets):
    answer = []
    visited = [False] * len(tickets)

    # 알파벳 순으로 먼저 탐색하기 위해 정렬
    tickets.sort()

    def dfs(current, path):
        nonlocal answer

        # 모든 티켓을 사용했다면 정답
        if len(path) == len(tickets) + 1:
            answer = path[:]
            return True

        for i in range(len(tickets)):
            start = tickets[i][0]
            end = tickets[i][1]

            # 현재 공항에서 출발하는 티켓이고,
            # 아직 사용하지 않은 티켓이면
            if start == current and not visited[i]:
                visited[i] = True
                path.append(end)

                if dfs(end, path):
                    return True

                # 실패하면 원상복구
                path.pop()
                visited[i] = False

        return False

    dfs("ICN", ["ICN"])

    return answer