import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(start_node):
    visit_list[start_node] = 1
    for i in range(1, n+1):
        if visit_list[i] == 0 and graph[start_node][i] == 1:
            dfs(i)

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visit_list = [0] * (n+1)
answer = 0

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = graph[node2][node1] = 1

for i in range(1, n+1):
    if not visit_list[i]:
        dfs(i)
        answer += 1

print(answer)

