import heapq

def dijkstra(x, y, n):
    queue = []
    heapq.heappush(queue, (graph[x][y], x, y))
    distance[x][y] = graph[x][y]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        dist, x, y = heapq.heappop(queue)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(queue, (cost, nx, ny))


t = int(input())

for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[1e9] * n for _ in range(n)]

    dijkstra(0, 0, n)

    print(distance[n-1][n-1])

# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
