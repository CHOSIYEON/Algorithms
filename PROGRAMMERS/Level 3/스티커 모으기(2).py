def cal(sticker):
    dp = [0] * len(sticker)
    dp[0], dp[1] = sticker[0], max(sticker[0], sticker[1])

    for i in range(2, len(sticker)):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])

    return max(dp)


def solution(sticker):
    answer = 0

    if len(sticker) == 1:
        return sticker[0]

    if len(sticker) == 2:
        return sticker[1]

    answer = max(answer, cal(sticker[:-1]))
    answer = max(answer, cal(sticker[1:]))

    return answer