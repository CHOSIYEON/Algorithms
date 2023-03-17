import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 0

    while queue:
        x, y = queue.popleft()
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return count


n = int(input())
data = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if data[i][j] == 1 and not visited[i][j]:
            answer.append(bfs(i, j))

print(len(answer))
answer.sort()

for i in answer:
    print(i)

