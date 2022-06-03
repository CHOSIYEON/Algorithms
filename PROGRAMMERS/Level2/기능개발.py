import math


def solution(progresses, speeds):
    answer = []
    idx = 0

    for i in range(len(progresses)):
        progresses[i] = math.ceil((100 - progresses[i]) / speeds[i])

    now = progresses[idx]
    cnt = 0

    while True:
        if idx >= len(progresses):
            break

        if progresses[idx] <= now:
            cnt += 1
        else:
            now = progresses[idx]
            answer.append(cnt)
            cnt = 1

        idx += 1

    answer.append(cnt)

    return answer