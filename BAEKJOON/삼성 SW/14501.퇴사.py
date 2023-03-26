import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n):
    for j in range(i + data[i][0], n + 1):
        if dp[j] < dp[i] + data[i][1]:
            dp[j] = dp[i] + data[i][1]

print(dp[-1])