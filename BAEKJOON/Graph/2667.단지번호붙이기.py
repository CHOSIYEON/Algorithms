import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny]:
                    graph[nx][ny] = 0
                    queue.append([nx, ny])
                    count += 1

    return count

n = int(input())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            answer.append(bfs(i, j))

print(len(answer))
answer.sort()
for i in answer:
    print(i)