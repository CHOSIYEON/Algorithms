import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque()
    queue.append((start,0))
    visited[start] = True

    while queue:
        node, dist = queue.popleft()
        distances[node] = dist
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append((i, dist+1))


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distances = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(x)

if k in distances:
    for idx, dist in enumerate(distances):
        if k == dist:
            print(idx)
else:
    print(-1)