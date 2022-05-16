def move_block(m, n, board):
    for y in range(n):
        for x in range(m - 1, -1, -1):
            if board[x][y] == '':
                nx = x - 1
                while nx >= 0:
                    if board[nx][y] != '':
                        board[x][y] = board[nx][y]
                        board[nx][y] = ''
                        break
                    else:
                        nx -= 1
    return board

def delete_block(m, n, board):
    delete = []

    for x in range(m - 1):
        for y in range(n - 1):
            if board[x][y] == '':
                continue

            if board[x][y] == board[x][y + 1] and board[x][y] == board[x + 1][y] and board[x][y] == board[x + 1][y + 1]:
                delete.append((x, y))
                delete.append((x + 1, y))
                delete.append((x, y + 1))
                delete.append((x + 1, y + 1))

    delete = set(delete)

    for x, y in delete:
        board[x][y] = ''

    return board, len(delete)


def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]
    board, count = delete_block(m, n, board)
    answer += count

    while count > 0:
        move_block(m, n, board)
        board, count = delete_block(m, n, board)
        answer += count

    return answer