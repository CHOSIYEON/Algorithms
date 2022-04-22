import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distances = [0] * (n+1)

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)

q = deque()
q.append((x, 0))
visited[x] = True

while q:
    node, dist = q.popleft()
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            distances[i] = dist + 1
            q.append((i, dist+1))

cnt = 0
for i in range(1, n+1):
    if distances[i] == k:
        print(i)
        cnt += 1

if cnt == 0:
    print(-1)