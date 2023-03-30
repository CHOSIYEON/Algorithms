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