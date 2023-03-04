n, k = map(int, input().split())
ans = 0

while True:
    target = n // k * k
    ans += (n-target)
    n = target

    if n < k:
        break
    ans += 1
    n //= k

ans += (n-1)
print(ans)