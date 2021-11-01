import sys
input = sys.stdin.readline

t = int(input())
arr = []

for i in range(t):
    n = int(input())
    arr.append(n)

dp = [0] * max(arr)

for i in range(max(arr)):
    if i == 0:
        dp[i] = 1
    elif i == 1:
        dp[i] = 2
    elif i == 2:
        dp[i] = 4
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in arr: 
    print(dp[i-1])