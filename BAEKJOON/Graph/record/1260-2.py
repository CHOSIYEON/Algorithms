import sys
from collections import deque
input = sys.stdin.readline

def dfs(start_node):
    visit[start_node] = 1
    print(start_node, end=' ')
    for i in graph[start_node]:
        if visit[i] == 0:
            dfs(i)

def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visit[start_node] = 1

    while queue:
        start_node = queue.popleft()
        print(start_node, end=' ')
        for i in graph[start_node]:
            if not visit[i]:
                queue.append(i)
                visit[i] = 1


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

dfs(v)
print()
visit = [0] * (n+1)
bfs(v)