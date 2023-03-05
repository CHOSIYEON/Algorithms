now = input()

dx = [-2, -2, 2, 2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, -2, -2, 2, 2]

x, y = ord(now[0])-96, int(now[1])
answer = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        answer += 1

print(answer)