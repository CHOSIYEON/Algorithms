def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1

    return score

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]
result = 0

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0)
print(result)

####

from collections import deque
import copy

def bfs():
    global result
    queue = deque()
    temp = copy.deepcopy(data)

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

    count = 0

    for i in range(n):
        count += temp[i].count(0)

    result = max(result, count)



def make_walls(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                make_walls(count + 1)
                data[i][j] = 0



n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]
result = 0

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

make_walls(0)

print(result)
