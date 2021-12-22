n, m, k = map(int, input().split())
ans = 0

while True:
    if n >= 2 and m >= 1:
        if n + m - 3 >= k:
            ans += 1
            n -= 2
            m -= 1
        else:
            break
    else:
        break

print(ans)