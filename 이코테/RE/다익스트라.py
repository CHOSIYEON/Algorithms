import heapq
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

# 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a 에서 b 로 가는 비용 c
    graph[a].append((b, c)) # 연결된 노드, 비용

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # start -> start 비용은 0
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])