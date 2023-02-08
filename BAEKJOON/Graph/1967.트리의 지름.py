import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def dfs(x, y):
    for i, j in graph[x]:
        if visited[i] == -1:
            visited[i] = j + y
            dfs(i, j + y)


n = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for _ in range(n-1):
    node1, node2, dist = map(int, input().split())
    graph[node1].append([node2, dist])
    graph[node2].append([node1, dist])

visited[1] = 0
dfs(1, 0)
start = visited.index(max(visited))

visited = [-1] * (n+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))
