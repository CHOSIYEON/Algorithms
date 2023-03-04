now = list(input())

x, y = int(now[1]), ord(now[0])
ans = 0

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 1 <= nx <= 8 and 97 <= ny <= 104:
        ans += 1

print(ans)