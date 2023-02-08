import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def dfs(node):
    visited[node] = True

    for i in tree[node]:
        if not visited[i]:
            answer[i] = node
            dfs(i)

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = {}

for _ in range(n-1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

dfs(1)
answer = sorted(answer.items(), key=lambda x: x[0])

for i in answer:
    print(i[1])