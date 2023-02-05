n = int(input())
data = [int(input()) for _ in range(n)]
dp = [0] * n

if n > 0:
    dp[0] = data[0]

if n > 1:
    dp[1] = data[0] + data[1]

if n > 2:
    dp[2] = max(dp[0] + data[2], data[1] + data[2])

for i in range(3, n):
    dp[i] = max(data[i] + data[i-1] + dp[i-3], data[i] + dp[i-2])

print(dp[-1])