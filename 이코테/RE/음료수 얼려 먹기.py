n, m = map(int, input().split())
ice = [list(map(int, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0

def dfs(x, y):
    ice[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if ice[nx][ny] == 0:
                dfs(nx, ny)


for i in range(n):
    for j in range(m):
        if ice[i][j] == 0:
            dfs(i, j)
            ans += 1

print(ans)