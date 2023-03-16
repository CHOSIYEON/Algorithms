import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while queue:
        z, x, y, time = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if data[nz][nx][ny] == 0:
                    data[nz][nx][ny] = 1
                    queue.append((nz, nx, ny, time + 1))

    check = True

    for z in range(h):
        for x in range(n):
            if 0 in data[z][x]:
                check = False

    if check:
        return time
    else:
        return -1


m, n, h = map(int, input().split())
data = [[] for _ in range(h)]
queue = deque()

for z in range(h):
    for _ in range(n):
        temp = list(map(int, input().split()))
        data[z].append(temp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for z in range(h):
    for x in range(n):
        for y in range(m):
            if data[z][x][y] == 1:
                queue.append((z, x, y, 0))

print(bfs())