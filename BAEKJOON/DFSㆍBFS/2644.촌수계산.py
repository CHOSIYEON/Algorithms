import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
data = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = -1

for _ in range(m):
    node1, node2 = map(int, input().split())
    data[node1].append(node2)
    data[node2].append(node1)

queue = deque()
queue.append((a, 0))

while queue:
    node, dist = queue.popleft()

    if node == b:
        answer = dist

    for i in data[node]:
        if not visited[i]:
            visited[i] = True
            queue.append((i, dist + 1))

print(answer)
