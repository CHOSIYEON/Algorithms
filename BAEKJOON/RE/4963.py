import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    else:
        if graph[x][y] == 1:
            graph[x][y] = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True

while True:
    w, h = map(int, input().split())
    graph = []
    ans = 0
    if w == 0 and h == 0:
        break
    else:
        for i in range(h):
            line = list(map(int, input().split()))
            graph.append(line)

        for x in range(h):
            for y in range(w):
                if dfs(x, y):
                    ans += 1

    print(ans)