import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(start):
    visited[start] = 1
    for i in range(n+1):
        if visited[i] == 0 and graph[start][i] == 1:
            dfs(i)

n, m = map(int, input().split())
visited = [0] * (n+1)
graph = [[0] * (n+1) for i in range(n+1)]
ans = 0

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = 1
    graph[node2][node1] = 1

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)