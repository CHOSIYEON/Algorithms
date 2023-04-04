from collections import deque

def move_cloud(d, s):
    increase = deque()
    prev_cloud = [[False] * n for _ in range(n)]

    while cloud:
        x, y = cloud.popleft()

        nx = (x + dx[d - 1] * s) % n
        ny = (y + dy[d - 1] * s) % n

        data[nx][ny] += 1
        increase.append((nx, ny))
        prev_cloud[nx][ny] = True

    while increase:
        x, y = increase.popleft()
        count = 0

        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] > 0:
                    count += 1

        data[x][y] += count

    for i in range(n):
        for j in range(n):
            if data[i][j] >= 2 and not prev_cloud[i][j]:
                cloud.append((i, j))
                data[i][j] -= 2


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
moves = [list(map(int, input().split())) for _ in range(m)]
cloud = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])

answer = 0

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for i in range(m):
    move_cloud(moves[i][0], moves[i][1])

for i in range(n):
    for j in range(n):
        if data[i][j] > 0:
            answer += data[i][j]

print(answer)