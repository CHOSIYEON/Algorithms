from collections import deque

def bfs():
    while q:
        virus, second, x, y = q.popleft()

        if second == target_s:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    q.append((virus, second + 1, nx, ny))


n, k = map(int, input().split())
graph = []
data = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

bfs()

if graph[target_x - 1][target_y - 1] == 0:
    print(0)
else:
    print(graph[target_x - 1][target_y - 1])


