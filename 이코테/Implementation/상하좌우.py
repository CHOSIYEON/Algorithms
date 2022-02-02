n = int(input())
cmds = list(map(str, input().split()))

cmds2 = ['L', 'R', 'U', 'D']

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1

for cmd in cmds:
    for i in range(len(cmds2)):
        if cmd == cmds2[i]:
            nx = x + dx[i]
            ny = y + dy[i]

            if 1 <= nx <= n and 1 <= ny <= n:
                x, y = nx, ny


print(x, y)