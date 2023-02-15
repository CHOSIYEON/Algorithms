from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x, y])
    graph[x][y] = 2

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append([nx, ny])

n, m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer += 1
            bfs(i, j)

print(answer)

# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
