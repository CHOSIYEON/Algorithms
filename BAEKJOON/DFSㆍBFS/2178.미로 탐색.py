import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().rstrip())) for _ in range(n)]
queue = deque()
queue.append((0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx, ny))

print(data[n-1][m-1])