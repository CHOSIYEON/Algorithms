import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            answer[i] = node
            dfs(i)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = [0] * (n+1)

for _ in range(n-1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

dfs(1)

for i in range(2, n+1):
    print(answer[i])
