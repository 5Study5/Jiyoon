def solution(name):
    answer = 0
    n = len(name)

    # 1. 위/아래 이동 횟수
    for i in range(n):
        up = ord(name[i]) - ord('A')
        down = ord('Z') - ord(name[i]) + 1

        answer += min(up, down)

    # 2. 좌/우 이동 횟수
    move = n - 1

    for i in range(n):
        next_i = i + 1

        # 연속된 A 찾기
        while next_i < n and name[next_i] == 'A':
            next_i += 1

        # 오른쪽으로 갔다가 다시 왼쪽으로 돌아가기
        case1 = 2 * i + (n - next_i)

        # 왼쪽으로 먼저 갔다가 오른쪽으로 돌아가기
        case2 = i + 2 * (n - next_i)

        move = min(move, case1, case2)

    answer += move

    return answer