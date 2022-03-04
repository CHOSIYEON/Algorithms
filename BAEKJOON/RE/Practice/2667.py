import sys
input = sys.stdin.readline

def dfs(x, y):
    global apt_cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        apt_cnt += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

n = int(input())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dangi_cnt = 0
apt_cnt = 0
apt_list = []

for i in range(n):
    tmp = list(map(int, input().strip()))
    graph.append(tmp)

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            if dfs(i, j):
                dangi_cnt +=1
                apt_list.append(apt_cnt)
                apt_cnt = 0

print(dangi_cnt)

apt_list.sort()
for i in apt_list:
    print(i)