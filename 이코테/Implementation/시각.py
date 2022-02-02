n = int(input())

ans = 0

for i in range(n+1):
    for j in range(60):
        for m in range(60):
            if '3' in str(i)+str(j)+str(m):
                ans += 1

print(ans)