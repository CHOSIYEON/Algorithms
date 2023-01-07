n = int(input())

arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]
dp3 = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(n):
    dp3[i] = dp[i] + dp2[i]


print(max(dp3)-1)