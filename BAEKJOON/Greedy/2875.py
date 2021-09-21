n, m, k = map(int, input().split())
total_team = 0

while True:
    if n >= 2 and m >= 1 and n + m >= k+3:
        total_team += 1
        n -= 2
        m -= 1
    else:
        break

print(total_team)