import heapq
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distances = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

q = []
q.append((0, 1))
distances[1] = 0

while q:
    dist, now = heapq.heappop(q)
    if distances[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if distances[i[0]] > cost:
            distances[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

answer = -1
distance = -INF
count = 0

for i in range(1, n+1):
    if distances[i] > distance:
        distance = distances[i]
        answer = i
        count = 1
    elif distances[i] == distance:
        count += 1

print(answer, distance, count, sep=' ')

# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2