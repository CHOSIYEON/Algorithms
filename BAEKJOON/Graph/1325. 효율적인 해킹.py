import sys
from collections import deque
input = sys.stdin.readline

def bfs(node, visited):
    queue = deque([node])
    visited[node] = True
    cnt = 0

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1

    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, n+1):
    answer.append(bfs(i, [False] * (n+1)))

max_value = max(answer)

for idx, value in enumerate(answer):
    if value == max_value:
        print(idx+1, end= ' ')
