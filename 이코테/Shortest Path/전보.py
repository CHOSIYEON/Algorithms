import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [1e9] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)

answer = 0
for i in range(1, n+1):
    if distance[i] != 1e9:
        answer += 1

print(answer-1, max(distance[1:]))

# case 1
# 3 2 1
# 1 2 4
# 1 3 2