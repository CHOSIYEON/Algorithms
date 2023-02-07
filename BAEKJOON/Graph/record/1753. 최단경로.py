import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

INF =1e9

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distances[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distances = [INF] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

dijkstra(start)

for i in range(1, len(distances)):
    if distances[i] == INF:
        print('INF')
    else:
        print(distances[i])