import sys
input = sys.stdin.readline
from collections import deque
import copy

def bfs():
    global answer
    queue = deque()
    temp = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
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

    answer = max(answer, count)

def make_walls(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_walls(count + 1)
                graph[i][j] = 0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = -1e9

make_walls(0)

print(answer)
