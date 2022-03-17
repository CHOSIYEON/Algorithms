import heapq
INF = 1e9

def dijstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distances[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distances = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

dijstra(1)

max_distance = -1e9
idx = -1
count = 0

for i in range(1, n+1):
    if max_distance < distances[i]:
        idx = i
        max_distance = distances[i]
        count = 0
    elif max_distance == distances[i]:
        count += 1

print(idx, max_distance, count+1, sep=' ')


