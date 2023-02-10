def cal(n, w):
    if n % (2 * w + 1) == 0:
        return n // (2 * w + 1)
    else:
        return (n // (2 * w + 1) + 1)


def solution(n, stations, w):
    answer = 0
    prev = 1

    for station in stations:
        dist = station - w - prev
        answer += cal(dist, w)
        prev = station + w + 1

    if prev <= n:
        dist = n - prev + 1
        answer += cal(dist, w)

    return answer

##

import math
def solution(n, stations, w):
    answer = 0
    idx = 1

    for i in stations:
        if i - w > 0:
            answer += math.ceil(((i - w) - idx) / (w * 2 + 1))
        idx = i + w + 1

    if idx - 1 < n:
        answer += math.ceil((n - (idx - 1)) / (w * 2 + 1))

    return answer