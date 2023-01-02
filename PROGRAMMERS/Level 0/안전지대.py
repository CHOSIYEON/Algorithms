def solution(board):
    answer = 0
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 1:
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] != 1:
                        board[nx][ny] = 2

    for x in range(len(board)):
        for y in range(len(board)):
            if not board[x][y]:
                answer += 1

    return answer