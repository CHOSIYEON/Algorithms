import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


for _ in range(n):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1

    curve = [d]

    for i in range(g):
        for j in range(len(curve) - 1, -1, -1):
            curve.append((curve[j] + 1) % 4)

    for i in curve:
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 101 and 0 <= ny < 101:
            graph[nx][ny] = 1
            x, y = nx, ny

answer = 0

for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
            answer += 1

print(answer)

