import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while data:
        virus, t, x, y = data.popleft()

        if t == s:
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    data.append((virus, t+1, nx, ny))

    return

n, k = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

s, target_x, target_y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

data.sort()
data = deque(data)

bfs()
print(graph[target_x-1][target_y-1])
