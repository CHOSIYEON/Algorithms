import sys
from collections import deque
input = sys.stdin.readline

def dfs(start_node):
    ans.append(str(start_node))
    visited[start_node] = 1

    for i in range(1, n+1):
        if visited[i] == 0 and graph[start_node][i] == 1:
            dfs(i)

def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = 1

    while queue:
        start_node = queue.popleft()
        ans.append(str(start_node))
        for i in range(1, n+1):
            if visited[i] == 0 and graph[start_node][i] == 1:
                queue.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
ans = []

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = graph[node2][node1] = 1

dfs(v)
print(' '.join(ans))
ans = []
visited = [0] * (n+1)
bfs(v)
print(' '.join(ans))