n, m = map(int, input().split())
a, b, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

directions = [0, 3, 2, 1]
steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
bsteps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

data[a][b] = -1

ans = 1

while True:
    turn_time = 0
    for _ in range(4):
        turn_time += 1
        next_direction = (d + 1) % 4
        na = a + steps[next_direction][0]
        nb = b + steps[next_direction][1]

        temp = data[na][nb]

        if temp == 0:
            ans += 1
            a = na
            b = nb
            data[na][nb] = -1
            d = next_direction
            break

        d = next_direction

    if turn_time == 4:
        na = a + bsteps[d][0]
        nb = b + bsteps[d][1]

        if data[na][nb] == 1:
            break
        else:
            a = na
            b = nb

print(ans)