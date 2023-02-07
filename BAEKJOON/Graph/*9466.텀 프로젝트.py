import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def dfs(node):
    global answer
    visited[node] = True
    cycle.append(node)

    for i in graph[node]:
        if not visited[i]:
            dfs(i)
        else:
            if i in cycle:
                answer += cycle[cycle.index(i):]


t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    nodes = list(map(int, input().split()))
    answer = []

    for node1, node2 in enumerate(nodes):
        graph[node1+1].append(node2)

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n-len(answer))


##############################################################

import sys
input = sys.stdin.readline
from collections import deque


def bfs(start):
    global answer
    queue = deque([start])
    visited[start] = True
    cycle.append(start)

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cycle.append(i)
            else:
                if i in cycle:
                    answer += cycle[cycle.index(i):]



t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    nodes = list(map(int, input().split()))
    answer = []

    for node1, node2 in enumerate(nodes):
        graph[node1+1].append(node2)

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            bfs(i)

    print(n-len(answer))