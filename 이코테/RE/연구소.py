import sys
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = -1e9

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def make_wall(count):
    if count == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                make_wall(count)
                count -= 1
                graph[i][j] = 0

def virus():
    queue = deque()
    temp = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))

    global ans
    temp_count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                temp_count += 1

    ans = max(ans, temp_count)

make_wall(0)
print(ans)