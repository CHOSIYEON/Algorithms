def toSecond(time):
    time = time.split(":")
    time = (int(time[0]) * 3600) + (int(time[1]) * 60) + int(time[2])
    return time

def solution(play_time, adv_time, logs):
    answer, max_value = 0, -1
    play_time = toSecond(play_time)
    adv_time = toSecond(adv_time)
    dp = [0] * (play_time + 1)

    for log in logs:
        start, end = log.split("-")
        start = toSecond(start)
        end = toSecond(end)

        dp[start] += 1
        dp[end] -= 1

    for i in range(1, play_time):
        dp[i] += dp[i - 1]

    for i in range(1, play_time):
        dp[i] += dp[i - 1]

    for i in range(adv_time - 1, play_time):
        temp = dp[i] - dp[i - adv_time]
        if max_value < temp:
            max_value = temp
            answer = i - adv_time + 1

    answer = str(answer // 3600).zfill(2) + ":" + str(answer % 3600 // 60).zfill(2) + ":" + str(answer % 3600 % 60).zfill(2)
    return answer