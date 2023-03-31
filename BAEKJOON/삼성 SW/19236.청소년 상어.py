import sys
input = sys.stdin.readline
import copy

def dfs(sx, sy, score, data):
    global answer

    score += data[sx][sy][0]
    answer = max(answer, score)
    data[sx][sy][0] = 0

    for f in range(1, 17):
        fx, fy = -1, -1

        for x in range(4):
            for y in range(4):
                if data[x][y][0] == f:
                    fx, fy = x, y
                    break

        if fx == -1 and fy == -1:
            continue

        fd = data[fx][fy][1]

        for i in range(8):
            nd = (fd + i) % 8

            nx = fx + directions[nd][0]
            ny = fy + directions[nd][1]

            if 0 > nx or nx >= 4 or 0 > ny or ny >= 4 or (nx == sx and ny == sy):
                continue

            data[fx][fy][1] = nd
            data[fx][fy], data[nx][ny] = data[nx][ny], data[fx][fy]
            break

    sd = data[sx][sy][1]

    for i in range(1, 5):
        nx = sx + directions[sd][0] * i
        ny = sy + directions[sd][1] * i

        if 0 <= nx < 4 and 0 <= ny < 4 and data[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(data))


data = [[] for _ in range(4)]
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
answer = 0


for i in range(4):
    temp = list(map(int, input().split()))

    for j in range(0, len(temp), 2):
        data[i].append([temp[j], temp[j + 1] - 1])

dfs(0, 0, 0, data)
print(answer)
