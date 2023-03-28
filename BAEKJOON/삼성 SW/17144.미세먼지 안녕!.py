import sys
input = sys.stdin.readline

def diffuse():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    diffused = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if data[x][y] <= 0:
                continue

            dust = data[x][y] // 5

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c and data[nx][ny] != -1:
                    diffused[nx][ny] += dust
                    diffused[x][y] -= dust

    for x in range(r):
        for y in range(c):
            data[x][y] += diffused[x][y]

def clean_dust_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    x, y, direction = m1, 1, 0
    prev = 0

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if x == m1 and y == 0:
            break

        if 0 > nx or nx >= r or 0 > ny or ny >= c:
            direction += 1
            continue

        data[x][y], prev = prev, data[x][y]
        x, y = nx, ny

def clean_dust_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y, direction = m2, 1, 0
    prev = 0

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if x == m2 and y == 0:
            break

        if 0 > nx or nx >= r or 0 > ny or ny >= c:
            direction += 1
            continue

        data[x][y], prev = prev, data[x][y]
        x, y = nx, ny


r, c, t = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(r)]
answer = 0

for i in range(r):
    if data[i][0] == -1:
        m1 = i
        m2 = i + 1
        break

for _ in range(t):
    diffuse()
    clean_dust_up()
    clean_dust_down()

for i in range(r):
    for j in range(c):
        if data[i][j] > 0:
            answer += data[i][j]

print(answer)

