import sys
input = sys.stdin.readline

def is_blue_again(x, y, d):
    d = reversed_directions[d]

    nx = x + directions[d][0]
    ny = y + directions[d][1]

    if 0 > nx or nx >= n or 0 > ny or ny >= n or board[nx][ny] == 2:
        return True
    return False

def move_next_pos(x, y, d):
    nx = x + directions[d][0]
    ny = y + directions[d][1]

    if 0 > nx or nx >= n or 0 > ny or ny >= n or board[nx][ny] == 2:
        if is_blue_again(x, y, d):
            return x, y, reversed_directions[d]
        else:
            d = reversed_directions[d]
            return move_next_pos(x, y, d)

    elif board[nx][ny] == 0:
        for value in record[x][y]:
            record[nx][ny].append(value)

            num, r, c, direct = horses_info[value]
            horses_info[value] = [num, nx, ny, direct]

        record[x][y] = []

    elif board[nx][ny] == 1:
        reversed_horse = record[x][y][::-1]

        for value in reversed_horse:
            record[nx][ny].append(value)

            num, r, c, direct = horses_info[value]
            horses_info[value] = [num, nx, ny, direct]

        record[x][y] = []

    return nx, ny, d


def is_bottom_horse(num, r, c):
    horse_state = record[r][c]

    if horse_state[0] == num:
        return True
    else:
        return False


def move_all_horses():
    for i in range(1, k + 1):
        num, r, c, d = horses_info[i]

        if not is_bottom_horse(num, r, c):
            continue

        nx, ny, nd = move_next_pos(r, c, d)
        horses_info[num] = [num, nx, ny, nd]



n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
record = [[[] for _ in range(n)] for _ in range(n)]
horses_info = [[] for _ in range(k + 1)]

directions = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
reversed_directions = {1: 2, 2: 1, 3: 4, 4: 3}

for i in range(1, k+1):
    r, c, d = map(int, input().split())
    horses_info[i] = [i, r - 1, c - 1, d]
    record[r - 1][c - 1].append(i)

def is_finish():
    for i in range(n):
        for j in range(n):
            if len(record[i][j]) >= 4:
                return True
    return False

answer = -1
time = 1
while time <= 1000:
    move_all_horses()

    if is_finish():
        answer = time
        break

    time += 1

print(answer)