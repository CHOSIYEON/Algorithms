import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    global ans
    queue = deque()
    queue.append([x, y])
    dist[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if dist[nx][ny] == -1:
                    if maze[nx][ny] == '0':
                        queue.appendleft([nx, ny])
                        dist[nx][ny] = dist[x][y]
                    elif maze[nx][ny] == '1':
                        queue.append([nx, ny])
                        dist[nx][ny] = dist[x][y] + 1


n, m = map(int, input().split())
maze = [list(input().strip()) for _ in range(m)]
dist = [[-1] * n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

bfs(0, 0)
print(dist[m-1][n-1])

###########################################################################

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, cnt):
    global ans
    queue = deque()
    queue.append([x, y, cnt])
    visited[x][y] = True

    while queue:
        x, y, cnt = queue.popleft()

        if x == m-1 and y == n-1:
            ans = min(ans, cnt)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if maze[nx][ny] == '1':
                    queue.append([nx, ny, cnt + 1])
                    visited[nx][ny] = True
                else:
                    queue.appendleft([nx, ny, cnt])
                    visited[nx][ny] = True


n, m = map(int, input().split())
maze = [list(input().strip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = sys.maxsize

bfs(0,0,0)
print(ans)