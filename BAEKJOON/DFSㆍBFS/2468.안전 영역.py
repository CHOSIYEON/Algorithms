import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, visited, temp):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if temp[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


def cal(h):
    visited = [[False] * n for _ in range(n)]
    temp = [[0] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if data[i][j] <= h:
                temp[i][j] = 0
            else:
                temp[i][j] = 1

    for i in range(n):
        for j in range(n):
            if temp[i][j] and not visited[i][j]:
                bfs(i, j, visited, temp)
                count += 1

    return count


n = int(input())
data = []
min_height, max_height = 1e9, -1e9
answer = -1e9

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    info = list(map(int, input().split()))
    data.append(info)
    max_height = max(max_height, max(info))

for height in range(max_height + 1):
    answer = max(answer, cal(height))

print(answer)
