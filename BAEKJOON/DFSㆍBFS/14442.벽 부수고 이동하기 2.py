import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        x, y, wall = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    queue.append((nx, ny, wall))

                elif data[nx][ny] == 1 and wall < k and visited[nx][ny][wall + 1] == 0:
                    visited[nx][ny][wall + 1] = visited[x][y][wall] + 1
                    queue.append((nx, ny, wall + 1))

    return -1



n, m, k = map(int, input().split())
data = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())