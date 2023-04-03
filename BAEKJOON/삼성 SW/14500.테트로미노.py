import sys
input = sys.stdin.readline

def dfs(x, y, score, count):
    global answer

    if count == 4:
        answer = max(answer, score)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, score + data[nx][ny], count + 1)
            visited[nx][ny] = False

def cal(x, y):
    global answer

    for i in range(4):
        score = data[x][y]

        for j in range(3):
            idx = (i + j) % 4
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                score = 0
                break

            score += data[nx][ny]

        answer = max(answer, score)

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, data[i][j], 1)
        visited[i][j] = False

        cal(i, j)

print(answer)
