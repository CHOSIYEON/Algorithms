import sys
input = sys.stdin.readline
from collections import deque

k = int(input())

def checkBinaryGraph(graph, v):
    visited = [-1] * (v+1)
    queue = deque()

    for i in range(1, v+1):
        if visited[i] == -1:
            visited[i] = True
            queue.append((i, True))
            while queue:
                n, subsetNum = queue.popleft()
                print(n, subsetNum)
                for now in graph[n]:
                    if visited[now] == -1:
                        visited[now] = not(subsetNum)
                        queue.append((now, not(subsetNum)))
                    else:
                        if visited[now] == subsetNum:
                            return False

    return True


for i in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for j in range(e):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
    if checkBinaryGraph(graph, v):
        print('YES')
    else:
        print('NO')

