import sys
input = sys.stdin.readline

def dfs(x, y, idx):
    if idx == len(target):
        return 1

    if visited[x][y][idx] != -1:
        return visited[x][y][idx]

    visited[x][y][idx] = 0

    for i in range(4):
        tx, ty = x, y
        for _ in range(k):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if words[nx][ny] == target[idx]:
                    visited[x][y][idx] += dfs(nx, ny, idx + 1)
            tx, ty = nx, ny

    return visited[x][y][idx]

n, m, k = map(int, input().split())
words = [list(input().rstrip()) for _ in range(n)]
target = input().rstrip()
visited = [[[-1] * len(target) for _ in range(m)] for _ in range(n)]
start = []
ans = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if words[i][j] == target[0]:
            start.append([i, j])

for i in start:
    x, y = i[0], i[1]
    ans += dfs(x, y, 1)

print(ans)
