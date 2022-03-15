import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque()
queue.append((x, 0))

visited[x] = True

while queue:
    node, dist = queue.popleft()
    if dist == k:
        answer.append(node)
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            queue.append((i, dist+1))


if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for dist in answer:
        print(dist)