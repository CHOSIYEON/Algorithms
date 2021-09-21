import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input().strip()) for _ in range(n)]
result = 0
idx = 0
coins.sort(reverse=True)

while k > 0:
    if coins[idx] <= k:
        result += k//coins[idx]
        k = k % coins[idx]
        idx += 1
    else:
        idx += 1

print(result)