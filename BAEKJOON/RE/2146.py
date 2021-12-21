import sys
from collections import deque
input = sys.stdin.readline

# 섬 구분하기
def bfs1(x, y):
    global count
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    graph[x][y] = count

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = count
                queue.append([nx, ny])

# 길찾기
def bfs2(z):
    global answer
    dist = [[-1] * n for _ in range(n)] # 거리
    queue = deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j] == z:
                queue.append([i, j])
                dist[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갈 수 없는 곳이면 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
            if graph[nx][ny] > 0 and graph[nx][ny] != z:
                answer = min(answer, dist[x][y])
                return
            # 바다를 만나면 dist를 1씩 늘린다.
            if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append([nx, ny])


n = int(input())
graph = []
visited = [[False] * n for _ in range(n)]
count = 1
answer = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            bfs1(i, j)
            count += 1


for i in range(1, count):
    bfs2(i)

print(answer)