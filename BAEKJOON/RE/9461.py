import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    if n <= 10:
        print(dp[n-1])
    else:
        for j in range(10, n):
            dp.append(dp[j-5] + dp[j-1])
        print(dp[-1])
