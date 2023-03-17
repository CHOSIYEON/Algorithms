import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, visited):
    global answer

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    united = []
    united_sum = 0

    while queue:
        x, y = queue.popleft()
        united.append((x, y))
        united_sum += data[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and l <= abs(data[nx][ny] - data[x][y]) <= r:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    if len(united) == 1:
        return False

    united_avg = united_sum // len(united)

    for x, y in united:
        data[x][y] = united_avg

    return True

n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    visited = [[False] * n for _ in range(n)]
    stop = True

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited):
                   stop = False

    if stop:
        break
    else:
        answer += 1

print(answer)

