import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0

while k > 0:
    for coin in coins:
        if coin <= k:
            ans = ans + k // coin
            k %= coin

print(ans)
