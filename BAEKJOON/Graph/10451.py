import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())

def dfs(graph, start_node, visited):
    visited[start_node] = 1
    for i in graph[start_node]:
        if visited[i] == 0:
            dfs(graph, i, visited)

for i in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    arr = list(map(int, input().split()))
    answer = 0

    for j in range(len(arr)):
        graph[j+1].append(arr[j])

    for m in range(1, n+1):
        if visited[m] == 0:
            dfs(graph, m, visited)
            answer += 1

    print(answer)