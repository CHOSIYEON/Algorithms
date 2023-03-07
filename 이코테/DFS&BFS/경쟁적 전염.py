import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))

virus.sort()
virus = deque(virus)

while virus:
    v, time, i, j = virus.popleft()

    if time == s:
        break

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[i][j]
                virus.append((graph[nx][ny], time + 1, nx, ny))

if graph[x - 1][y - 1] != 0:
    print(graph[x - 1][y - 1])
else:
    print(0)