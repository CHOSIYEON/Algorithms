n = int(input())
dp = [1] * (n + 1)

for i in range(1, n + 1):
    if i % 2 == 0:
        dp[i] = 2 * dp[i - 1] + 1
    else:
        dp[i] = 2 * dp[i - 1] - 1

print(dp[-1] % 10007)