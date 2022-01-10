import sys
input = sys.stdin.readline

def dfs(x, y, count):
    global ans
    ans = max(ans, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and not alpha[ord(maps[nx][ny]) - 65]:
            alpha[ord(maps[nx][ny]) - 65] = 1
            dfs(nx, ny, count + 1)
            alpha[ord(maps[nx][ny]) - 65] = 0

r, c = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
alpha = [0] * 26
alpha[ord(maps[0][0]) - 65] = 1
ans = 1

dfs(0, 0, 1)
print(ans)



