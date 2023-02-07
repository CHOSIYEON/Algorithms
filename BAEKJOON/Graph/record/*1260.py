import sys
from collections import deque
input = sys.stdin.readline

def dfs(start_node):
    visit_list[start_node] = 1
    print(start_node, end=' ')

    for i in range(1, n+1):
        if visit_list[i] == 0 and graph[start_node][i] == 1:
            dfs(i)

def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visit_list[start_node] = 1

    while queue:
        start_node = queue.popleft()
        print(start_node, end=' ')
        for i in range(1, n+1):
            if visit_list[i] == 0 and graph[start_node][i] == 1:
                queue.append(i)
                visit_list[i] = 1

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visit_list = [0] * (n+1)

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = graph[node2][node1] = 1

dfs(v)
print()
visit_list = [0] * (n+1)
bfs(v)