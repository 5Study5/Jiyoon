def solution(n):
    answer = 0
    board = [-1] * n

    def dfs(row):
        nonlocal answer

        # n개의 퀸을 모두 배치한 경우
        if row == n:
            answer += 1
            return

        # 현재 row에서 어느 열에 놓을지 확인
        for col in range(n):
            possible = True

            # 이전에 놓은 퀸들과 비교
            for prev_row in range(row):
                prev_col = board[prev_row]

                # 같은 열
                if prev_col == col:
                    possible = False
                    break

                # 같은 대각선
                if abs(row - prev_row) == abs(col - prev_col):
                    possible = False
                    break

            # 놓을 수 있다면
            if possible:
                board[row] = col
                dfs(row + 1)
                board[row] = -1

    dfs(0)

    return answer