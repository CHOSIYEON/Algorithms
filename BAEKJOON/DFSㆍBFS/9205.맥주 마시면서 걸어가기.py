import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque()
    queue.append((house_x, house_y))

    while queue:
        x, y = queue.popleft()

        if abs(x - festival_x) + abs(y - festival_y) <= 1000:
            return 'happy'

        for i in range(n):
            if not visited[i]:
                con_x, con_y = data[i]

                if abs(con_x - x) + abs(con_y - y) <= 1000:
                    queue.append((con_x, con_y))
                    visited[i] = True

    return 'sad'

t = int(input())

for _ in range(t):
    n = int(input())
    house_x, house_y = map(int, input().split())
    data = []
    visited = [False] * (n + 1)

    for _ in range(n):
        data.append(list(map(int, input().split())))

    festival_x, festival_y = map(int, input().split())

    print(bfs())