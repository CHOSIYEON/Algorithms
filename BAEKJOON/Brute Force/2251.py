from collections import deque

def check(x, y):
    if not visited[x][y]:
        visited[x][y] = 1
        queue.append([x, y])

def bfs():

    while queue:
        x, y = queue.popleft()
        z = c - x - y

        if x == 0:
            ans.append(z)

        # a -> b
        water = min(x, b - y)
        nx, ny = x - water, y + water
        check(nx, ny)
        # b -> a
        water = min(y, a - x)
        nx, ny = x + water, y - water
        check(nx, ny)
        # a -> c
        water = min(x, c - z)
        nx = x - water
        check(nx, y)
        # c -> a
        water = min(z, a - x)
        nx = x + water
        check(nx, y)
        # b -> c
        water = min(y, c - z)
        ny = y - water
        check(x, ny)
        # c -> b
        water = min(z, b - y)
        ny = y + water
        check(x, ny)


a, b, c = map(int, input().split())
total = c
ans = []
visited = [[0] * (b+1) for _ in range(a+1)]
queue = deque()
queue.append([0, 0])
visited[0][0] = 1

bfs()
ans.sort()

for i in ans:
    print(i, end=' ')