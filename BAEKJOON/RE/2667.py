import sys
input = sys.stdin.readline

def dfs(x, y):
    global house_count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        house_count += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n = int(input())
graph = []
visited = [[0] * n for _ in range(n)]

for i in range(n):
    line = list(map(int,input().strip()))
    graph.append(line)

dangi_count = 0
dangi = []
house_count = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            dangi_count += 1
            dangi.append(house_count)
            house_count = 0

print(dangi_count)
dangi.sort()
for i in dangi:
    print(i)
