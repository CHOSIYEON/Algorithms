import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny]:
                    queue.append([nx, ny])
                    graph[nx][ny] = 0


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []
    visited = [[False] * w] * h
    answer = 0

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j]:
                answer += 1
                bfs(i, j)

    print(answer)