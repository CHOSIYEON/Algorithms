def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원리스트)
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

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원리스트)
visited = [False] * 9

dfs(graph, 1, visited)

#########################################

def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')

    for i in range(1, len(graph)):
        if visited[i] == 0 and graph[visited][i] == 1:
            dfs(i)