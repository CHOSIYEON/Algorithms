import sys
input = sys.stdin.readline

t = int(input())

def sol(dp):
    for i in range(1, len(dp[0])):
        if i == 1:
            dp[0][i] += dp[1][i-1]
            dp[1][i] += dp[0][i-1]
        else:
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][-1], dp[1][-1]))


for i in range(t):
    n = int(input())
    dp = []
    for j in range(2):
        arr = list(map(int, input().split()))
        dp.append(arr)
    sol(dp)