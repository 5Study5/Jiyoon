def solution(board):
    rows = len(board)
    cols = len(board[0])

    max_size = 0 # 한 변 길이

    for i in range(rows):
        for j in range(cols):

            if board[i][j] == 1:
                if i == 0 or j == 0:
                    board[i][j] = 1
                else:
                    board[i][j] = min(
                        board[i-1][j],
                        board[i][j-1],
                        board[i-1][j-1]
                    ) + 1

                max_size = max(max_size, board[i][j])

    return max_size ** 2