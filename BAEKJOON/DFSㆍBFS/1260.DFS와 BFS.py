import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

def dfs(node):
    visited[node] = True
    print(node, end=' ')

    for i in graph[node]:
        if not visited[i]:
            dfs(i)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)

