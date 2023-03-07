import heapq
from collections import deque

def bfs():
    queue = deque()
    queue.append((1, 0))
    visited[1] = True

    while queue:
        now, dist = queue.popleft()
        distance[now] = dist

        for i in graph[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append((i[0], dist + 1))

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 1))
    distance[1] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))



n, m = map(int, input().split())
distance = [1e9] * (n+1)
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

# dijkstra()

bfs()

max_distance = max(distance[1:])
print(distance.index(max_distance), max_distance, distance.count(max_distance))