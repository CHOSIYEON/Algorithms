info = input()
row = int(info[1])
col = ord(info[0]) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

ans = 0

for step in steps:
    nr = row + step[0]
    nc = col + step[1]

    if 1 <= nr <= 8 and 1 <= nc <= 8:
        ans += 1

print(ans)