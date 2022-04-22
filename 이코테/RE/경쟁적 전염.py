import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, ans_x, ans_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            heapq.heappush(queue, (0, graph[i][j], i, j))

while queue:
    time, virus, x, y = heapq.heappop(queue)

    if time == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                heapq.heappush(queue, (time+1, graph[nx][ny], nx, ny))

print(graph[ans_x-1][ans_y-1])
