import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))

    union = [(x, y)]
    visited[x][y] = True
    union_summary = people[x][y]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(people[x][y] - people[nx][ny]) <= r:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    union.append((nx, ny))
                    union_summary += people[nx][ny]

    if len(union) == 1:
        return False

    for x, y in union:
        people[x][y] = union_summary // len(union)

    return True



n, l, r = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    visited = [[False] * n for _ in range(n)]
    stop = True

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    stop = False

    if stop:
        break
    else:
        answer += 1

print(answer)