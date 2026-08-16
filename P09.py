# 아이디어만...
# key를 회전/이동 시킬 때, 행+열 다같이 더함
# 같은 행과 열에 있는 key + lock 했을 때, lock 전부 1


def solution(key, lock):
    m = len(key)
    n = len(lock)

    # 큰 보드 생성
    board_size = n + 2 * (m - 1)
    board = [[0] * board_size for _ in range(board_size)]

    # 가운데에 lock 배치
    for i in range(n):
        for j in range(n):
            board[i + m - 1][j + m - 1] = lock[i][j]

    # 4번 회전
    for _ in range(4):

        # key를 이동시켜보기
        for row in range(board_size - m + 1):
            for col in range(board_size - m + 1):

                # key를 board에 더하기
                for i in range(m):
                    for j in range(m):
                        board[row + i][col + j] += key[i][j]

                # lock 부분이 모두 1인지 확인
                if check(board, m, n):
                    return True

                # 다시 원상복구
                for i in range(m):
                    for j in range(m):
                        board[row + i][col + j] -= key[i][j]

        # key 90도 회전
        key = rotate(key)

    return False


def check(board, m, n):
    for i in range(n):
        for j in range(n):
            if board[i + m - 1][j + m - 1] != 1:
                return False

    return True


def rotate(key):
    m = len(key)

    rotated = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            rotated[j][m - 1 - i] = key[i][j]

    return rotated