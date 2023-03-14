import sys
import copy
input = sys.stdin.readline
from collections import deque

def cal():
    queue = deque()
    temp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            temp[i][j] = data[i][j]

            if temp[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))

    count = 0

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1

    return count


def make_wall(count):
    global answer

    if count == 3:
        answer = max(answer, cal())
        return

    for i, j in empty:
        if data[i][j] == 0:
            data[i][j] = 1
            make_wall(count + 1)
            data[i][j] = 0

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
empty = []
answer = -1e9

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            empty.append((i, j))

make_wall(0)

print(answer)