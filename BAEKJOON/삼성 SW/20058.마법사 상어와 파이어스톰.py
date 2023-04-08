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
                if not visited[nx][ny] and data[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return count

def seperate(l):
    rotated = [[0] * n for _ in range(n)]
    length = 2 ** l

    for x in range(0, n, length):
        for y in range(0, n, length):
            for i in range(length):
                for j in range(length):
                    rotated[j + x][length - i - 1 + y] = data[i + x][j + y]

    meltings = []

    for x in range(n):
        for y in range(n):
            count = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if rotated[nx][ny] > 0:
                        count += 1

            if count < 3:
                meltings.append((x, y))

    for x, y in meltings:
        rotated[x][y] -= 1

    return rotated


n, q = map(int, input().split())
n = 2 ** n
data = [list(map(int, input().split())) for _ in range(n)]
steps = list(map(int, input().split()))
visited = [[False] * n for _ in range(n)]
answer1, answer2 = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for step in steps:
    data = seperate(step)

for i in range(n):
    for j in range(n):
        if data[i][j] > 0:
            answer1 += data[i][j]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and data[i][j] > 0:
            answer2 = max(answer2, bfs(i, j))

print(answer1)
print(answer2)
