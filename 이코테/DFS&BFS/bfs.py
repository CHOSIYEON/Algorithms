from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)


#################################

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        start_node = queue.popleft()
        print(start_node, end=' ')
        for i in range(1, n+1):
            if visited[i] == 0 and graph[start_node][i] == 1:
                queue.append(i)
                visited[i] = 1