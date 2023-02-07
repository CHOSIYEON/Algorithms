import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = 0

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        answer += 1

print(answer)