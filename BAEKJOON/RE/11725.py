import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i)


n = int(input())
tree = [[] for _ in range(n+1)]
parents = [0] * (n+1)

for i in range(n-1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

dfs(1)

for i in range(2, n+1):
    print(parents[i])

