import sys
input = sys.stdin.readline
import copy

def fill(x, y, direction, temp):
    for d in direction:
        nx, ny = x, y

        while True:
            nx += dx[d]
            ny += dy[d]

            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                break

            if temp[nx][ny] == 6:
                break

            if temp[nx][ny] == 0:
                temp[nx][ny] = '#'


def dfs(idx, data):
    global answer

    if idx == len(cctv):
        count = 0
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    count += 1

        answer = min(answer, count)
        return

    temp = copy.deepcopy(data)
    type, x, y = cctv[idx]

    for d in directions[type]:
        fill(x, y, d, temp)
        dfs(idx + 1, temp)
        temp = copy.deepcopy(data)


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
cctv = []
directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 1e9

for i in range(n):
    for j in range(m):
        if 1 <= data[i][j] <= 5:
            cctv.append((data[i][j], i, j))

dfs(0, data)
print(answer)