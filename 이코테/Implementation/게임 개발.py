n, m = map(int, input().split())
x, y, direction = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

directions = [0, 3, 2, 1]
steps = {0: (-1, 0), 3: (0, -1), 2: (1, 0), 1: (0, 1)}
now = directions.index(direction)
answer = 0

visited[x][y] = True

while True:
    for i in range(4):
        to = directions[(now + 1) % 4]
        nx = x + steps[to][0]
        ny = y + steps[to][1]

        now = (now + 1) % 4

        if not visited[nx][ny] and not info[nx][ny]:
            visited[nx][ny] = True
            x, y = nx, ny
            answer += 1
            break
    else:
        nx = x + (-1) * steps[now][0]
        ny = y + (-1) * steps[now][1]

        if info[nx][ny]:
            break
        else:
            x, y = nx, ny
            answer += 1

print(answer)