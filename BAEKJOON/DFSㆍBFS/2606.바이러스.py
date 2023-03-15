import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
data = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = 0

queue = deque()
queue.append(1)
visited[1] = True

for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

while queue:
    node = queue.popleft()
    answer += 1

    for i in data[node]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)

print(answer - 1)
