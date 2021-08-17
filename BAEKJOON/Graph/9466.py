import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000001)

t = int(input())

def dfs(graph, start_node, visited):
    global result
    visited[start_node] = 1
    cycle.append(start_node)

    next_node = graph[start_node][0]

    if visited[next_node] == 0:
        dfs(graph, next_node, visited)
    else:
        if next_node in cycle:
            result += cycle[cycle.index(next_node):]


for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    result = []

    for j in range(len(arr)):
        graph[j+1].append(arr[j])

    for m in range(1, n+1):
        if visited[m] == 0:
            cycle = []
            dfs(graph, m, visited)

    print(len(arr)-len(result))




