import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    nodes = list(map(int, input().split()))
    answer = 0

    for node1, node2 in enumerate(nodes):
        graph[node1+1].append(node2)

    for i in range(1, n+1):
        if not visited[i]:
            bfs(i)
            answer += 1

    print(answer)