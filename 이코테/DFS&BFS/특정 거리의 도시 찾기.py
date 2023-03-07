import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in cities[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m, k, x = map(int, input().split())
cities = [[] for _ in range(n+1)]
distance = [1e9] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    cities[a].append((b, 1))

dijkstra(x)
count = 0

for idx, value in enumerate(distance):
    if value == k:
        print(idx)
        count += 1

if count == 0:
    print(-1)