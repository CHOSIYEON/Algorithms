import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])


m, n = map(int, input().split())
answer = 0
graph = []
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))

print(answer-1)