n = int(input())
cmd = map(str, input().split())
x, y = 1, 1
nx, ny = 0, 0

for i in cmd:
    if i == 'R':
        nx = x
        ny = y + 1
    elif i == 'L':
        nx = x
        ny = y - 1
    elif i == 'U':
        nx = x - 1
        ny = y
    elif i == 'D':
        nx = x + 1
        ny = y

    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny

print(x, y)