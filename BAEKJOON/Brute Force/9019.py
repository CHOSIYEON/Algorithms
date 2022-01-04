import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    queue = deque()
    queue.append([a, ''])
    visited = [0] * 10001

    while queue:
        x, cmd = queue.popleft()
        visited[x] = 1

        if x == b:
            return cmd

        # D
        if not visited[x * 2 % 10000]:
            visited[x * 2 % 10000] = True
            queue.append([x * 2 % 10000, cmd + "D"])
        # S
        if not visited[(x - 1) % 10000]:
            visited[(x - 1) % 10000] = True
            queue.append([(x - 1) % 10000, cmd + "S"])
        # L
        if not visited[x % 1000 * 10 + x // 1000]:
            visited[x % 1000 * 10 + x // 1000] = True
            queue.append([x % 1000 * 10 + x // 1000, cmd + "L"])
        # R
        if not visited[x % 10 * 1000 + x // 10]:
            visited[x % 10 * 1000 + x // 10] = True
            queue.append([x % 10 * 1000 + x // 10, cmd + "R"])


t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))

