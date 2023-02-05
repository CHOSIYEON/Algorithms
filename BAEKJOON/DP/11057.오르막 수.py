n = int(input())
dp = [[1 for _ in range(10)] for _ in range(n)]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(sum(dp[-1]) % 10007)