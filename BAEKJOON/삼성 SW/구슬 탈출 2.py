import sys
input = sys.stdin.readline
from collections import deque

def move(x, y, dx, dy):
    count = 0

    while data[x + dx][y + dy] != 'O' and data[x + dx][y + dy] != '#':
        x += dx
        y += dy
        count += 1

    return x, y, count

def bfs():
    while queue:
        rx, ry, bx, by, count = queue.popleft()

        if count > 10:
            return -1

        for i in range(4):
            nx_r, ny_r, count_r = move(rx, ry, dx[i], dy[i])
            nx_b, ny_b, count_b = move(bx, by, dx[i], dy[i])

            if data[nx_b + dx[i]][ny_b + dy[i]] == 'O':
                continue

            if data[nx_r + dx[i]][ny_r + dy[i]] == 'O':
                return count

            if nx_r == nx_b and ny_r == ny_b:
                if count_r > count_b:
                    nx_r -= dx[i]
                    ny_r -= dy[i]
                else:
                    nx_b -= dx[i]
                    ny_b -= dy[i]

            if (nx_r, ny_r, nx_b, ny_b) not in visited:
                visited.append((nx_r, ny_r, nx_b, ny_b))
                queue.append((nx_r, ny_r, nx_b, ny_b, count + 1))

    return -1

n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(n)]
rx, ry, bx, by = 0, 0, 0, 0
visited = []
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if data[i][j] == 'R':
            rx, ry = i, j
        elif data[i][j] == 'B':
            bx, by = i, j

visited.append((rx, ry, bx, by))
queue.append((rx, ry, bx, by, 1))

print(bfs())
