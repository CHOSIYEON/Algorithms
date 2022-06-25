def solution(n):
    if n % 2 == 1:
        return 0

    dp = [3, 11]

    for i in range(2, n // 2 + 1, 1):
        dp.append(((dp[i - 1] * 4 % 1000000007) - dp[i - 2] % 1000000007 + 1000000007) % 1000000007)

    return dp[n // 2 - 1]