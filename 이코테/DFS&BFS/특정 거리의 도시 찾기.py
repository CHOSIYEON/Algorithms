from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_node):
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if distance[i] == -1:
                distance[i] = distance[node] + 1
                queue.append(i)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
distance[x] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(x)
cnt = 0

for idx, i in enumerate(distance):
    if i == k:
        print(idx)
        cnt += 1

if cnt == 0:
    print(-1)

