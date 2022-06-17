import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end= ' ')
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(start):
    visited[start] = True
    print(start, end= ' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(n+1):
    graph[i] = sorted(graph[i])

dfs(v)
print()

visited = [False] * (n+1)
bfs(v)