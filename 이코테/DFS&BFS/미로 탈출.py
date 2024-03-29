from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

n, m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input())))

bfs(0, 0)
print(graph[-1][-1])

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111