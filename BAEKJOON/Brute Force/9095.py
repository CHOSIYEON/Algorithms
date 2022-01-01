import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

def ans(num):
    dp = []

    dp.append(1)
    dp.append(2)
    dp.append(4)

    for i in range(3, num):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    print(dp[num-1])

for i in arr:
    ans(i)