from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0))
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True

    available = []

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if 0 < data[nx][ny] < shark:
                    visited[nx][ny] = True
                    available.append((data[nx][ny], nx, ny, dist + 1))
                    queue.append((nx, ny, dist + 1))
                elif data[nx][ny] == shark or data[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

    if len(available) == 0:
        return (-1, -1, -1, -1)

    available.sort(key=lambda x: (x[3], x[1], x[2]))

    return available[0]

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
shark = 2
shark_x, shark_y = -1, -1
prev, count = 2, 0
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            shark_x, shark_y = i, j
            data[i][j] = 0

while True:
    fish, x, y, dist = bfs(shark_x, shark_y)

    if fish == -1:
        break

    count += 1
    answer += dist

    if prev == count:
        shark += 1
        prev = shark
        count = 0

    data[x][y] = 0
    shark_x, shark_y = x, y

print(answer)





