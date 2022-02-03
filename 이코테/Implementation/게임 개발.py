n, m = map(int, input().split())
x, y, direction = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

visited[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

bx = [1, 0, -1, 0]
by = [0, 1, 0, -1]

directions = [0, 3, 2, 1]
now = directions.index(direction)

ans = 0
flag = 0

while True:
    flag = 0
    for i in range(4):
        now += 1
        if now >= 4:
            now %= 4

        nx = x + dx[now]
        ny = y + dy[now]

        if visited[nx][ny] == 0 and map_info[nx][ny] != 1:
            x, y = nx, ny
            visited[nx][ny] = 1
            ans += 1
            break

        if i == 3:
            flag = 1

    if flag:
        nx = x + bx[now]
        ny = y + by[now]

        if map_info[nx][ny] != 1:
            x, y = nx, ny
            ans += 1
        else:
            break

print(ans)