from collections import deque

def bfs(selected):
    active = deque()
    temp = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    result = 0

    for i in range(n):
        for j in range(n):
            if data[i][j] == 1:
                temp[i][j] = -2
            elif data[i][j] == 2:
                temp[i][j] = -3

    for i in selected:
        temp[virus[i][0]][virus[i][1]] = -1
        active.append((virus[i][0], virus[i][1], 1))

    while active:
        x, y, time = active.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = time
                    visited[nx][ny] = True
                    active.append((nx, ny, time + 1))
                elif temp[nx][ny] == -3:
                    visited[nx][ny] = True
                    active.append((nx, ny, time + 1))

    for i in range(n):
        for j in range(n):
            if temp[i][j] == 0:
                return -1

    for row in temp:
        result = max(result, max(row))

    return result

def dfs(idx, selected):
    global answer

    if len(selected) == m:
        time = bfs(selected)

        if time != -1:
            answer = min(answer, time)
        return

    for i in range(idx, len(virus)):
        if not visited[i]:
            visited[i] = True
            selected.append(i)
            dfs(i + 1, selected)
            selected.pop()
            visited[i] = False

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
virus = deque()
answer = 1e9

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            virus.append((i, j))

visited = [False] * len(virus)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0, [])

if answer == 1e9:
    print(-1)
else:
    print(answer)