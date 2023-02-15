from collections import deque
import sys

def bfs(start):
    queue = deque()
    queue.append(start)

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
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)

bfs(x)
count = 0

for idx, dist in enumerate(distance):
    if dist == k:
        print(idx)
        count += 1

if count == 0:
    print(-1)

###

from collections import deque
import sys


def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if distance[i] == -1:
                distance[i] = distance[node] + 1
                queue.append(i)


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)
distance[x] = 0

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)

bfs(x)
count = 0

for idx, dist in enumerate(distance):
    if dist == k:
        print(idx)
        count += 1

if count == 0:
    print(-1)