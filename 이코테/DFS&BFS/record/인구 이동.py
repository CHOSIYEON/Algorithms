import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph, visit):
    unit = []
    people = 0

    q = deque()
    q.append((x, y))
    unit.append((x, y))
    people += graph[x][y]
    visit[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] != True:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    unit.append((nx, ny))
                    people += graph[nx][ny]
                    visit[nx][ny] = True

    newPeople = people // len(unit)

    for x, y in unit:
        graph[x][y] = newPeople

    if len(unit) >= 2:
        return True
    else:
        return False


result = 0

while True:
    visit = [[False] * n for _ in range(n)]
    stop = True

    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                if bfs(i, j, data, visit):
                    stop = False

    if stop:
        break
    else:
        result += 1

print(result)