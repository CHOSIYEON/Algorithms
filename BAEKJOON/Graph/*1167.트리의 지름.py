import sys
input = sys.stdin.readline

def dfs(x, y):
    for i, j in graph[x]:
        if visited[i] == -1:
            visited[i] = j + y
            dfs(i, j + y)

v = int(input())
graph = [[] for _ in range(v+1)]
visited = [-1] * (v+1)

for _ in range(v):
    info = list(map(int, input().split()))

    for i in range(1, len(info)-2, 2):
        graph[info[0]].append([info[i], info[i+1]])

visited[1] = 0
dfs(1, 0)
start = visited.index(max(visited))
visited = [-1] * (v+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))