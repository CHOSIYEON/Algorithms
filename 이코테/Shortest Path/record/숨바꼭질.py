from collections import deque

def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        node, dist = queue.popleft()
        distances[node] = dist
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, dist+1))



n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distances = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


bfs(1)

max_distance = max(distances)
idxs = []
count = 0

for idx, dist in enumerate(distances):
    if dist == max_distance:
        idxs.append(idx)
        count += 1

print(min(idxs), max_distance, count, sep=' ')