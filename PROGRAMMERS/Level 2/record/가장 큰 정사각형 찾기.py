def solution(board):
    answer = 0 if not board[0][0] else 1

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j]:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                answer = max(answer, board[i][j])

    return answer * answer

# 정확도 O, 시간 초과
def find_max(board, l, x, y):
    for i in range(x, x + l, 1):
        for j in range(y, y + l, 1):
            if not board[i][j]:
                return False
    return True


def solution(board):
    row, col = len(board), len(board[0])
    max_l = min(row, col)

    for l in range(max_l, 0, -1):
        for i in range(0, row - l + 1, 1):
            for j in range(0, col - l + 1, 1):
                if find_max(board, l, i, j):
                    return l * l
    return 0

