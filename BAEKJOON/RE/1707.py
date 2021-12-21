import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        start = queue.popleft()
        for i in graph[start]:
            if visited[i] == 0:
                visited[i] = -visited[start]
                queue.append(i)
            elif visited[i] == visited[start]:
                return False
    return True


k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    ans = True

    for _ in range(e):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    for i in range(1, v+1):
        if visited[i] == 0:
            if bfs(i) == 0:
                ans = False
                break

    if ans:
        print("YES")
    else:
        print("NO")


