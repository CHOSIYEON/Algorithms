n = int(input())
data = list(map(int, input().split()))
dp, dp2 = [1] * n, [1] * n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

data = data[::-1]

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2 = dp2[::-1]

result = 0

for i in range(n):
    result = max(result, dp[i] + dp2[i])

print(result - 1)