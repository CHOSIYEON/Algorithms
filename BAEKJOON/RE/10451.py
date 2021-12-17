import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)


t = int(input())

for i in range(t):
    n = int(input())
    visited = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    node = list(map(int, input().split()))

    for j in range(len(node)):
        graph[j+1].append(node[j])

    ans = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            ans += 1

    print(ans)