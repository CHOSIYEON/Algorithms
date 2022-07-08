import heapq

def dijkstra(start, distance, graph):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(n, s, a, b, fares):
    answer = 1e9
    graph = [[] for _ in range(n + 1)]
    distance = [1e9] * (n + 1)

    for fare in fares:
        node1, node2, cost = fare
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))

    dijkstra(s, distance, graph)

    for i in range(1, n + 1):
        distance2 = [1e9] * (n + 1)
        dijkstra(i, distance2, graph)

        if answer > distance[i] + distance2[a] + distance2[b]:
            answer = distance[i] + distance2[a] + distance2[b]

    return answer