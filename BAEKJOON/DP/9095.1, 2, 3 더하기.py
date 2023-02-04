t = int(input())
arr = [int(input()) for _ in range(t)]
dp = [0] * (max(arr) + 2)

dp[0], dp[1], dp[2] = 1, 2, 4

for i in range(3, len(dp)):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for num in arr:
    print(dp[num - 1])