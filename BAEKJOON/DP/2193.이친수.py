n = int(input())
dp = [[0, 1] for _ in range(n)]

for i in range(1, n):
    for j in range(2):
        if j == 0:
            dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
        else:
            dp[i][j] = dp[i-1][j-1]

print(sum(dp[-1]))