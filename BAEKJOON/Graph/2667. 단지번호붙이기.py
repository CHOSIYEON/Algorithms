import sys
input = sys.stdin.readline

def dfs(x, y, dangi):
    global cnt
    graph[x][y] = dangi
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                graph[nx][ny] = dangi
                dfs(nx, ny, dangi)

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
answer = []
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j, len(answer) + 2)
            answer.append(cnt)
            cnt = 0

print(len(answer))
answer.sort()
for i in answer:
    print(i)

