n = int(input())
ans = 0

for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            temp = str(hour)+str(minute)+str(second)
            if '3' in temp:
                ans += 1

print(ans)