from collections import deque

def dfs(start_node):
    visited[start_node] = 1
    print(start_node, end=' ')

    for i in range(1, n+1):
        if graph[start_node][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = 1

    while queue:
        node = queue.popleft()
        print(node, end = ' ')
        for i in range(1, n+1):
            if graph[node][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = 1
    graph[node2][node1] = 1

dfs(v)
visited = [0] * (n+1)
print()
bfs(v)