n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
ans = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1


def dfs(start_node):
    visited[start_node] = 1

    for i in range(1, n + 1):
        if graph[start_node][i] == 1 and visited[i] == False:
            dfs(i)

for i in range(1, n+1):
    if visited[i] != True:
        dfs(i)
        ans += 1

print(ans)