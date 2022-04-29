def solution(N, stages):
    answer = []
    data = [0] * (N + 1)
    fail = [[x, 0] for x in range(N)]

    for stage in stages:
        data[stage - 1] += 1

    total = sum(data)

    for i in range(N):
        if total == 0:
            continue

        fail[i][1] = data[i] / total
        total -= data[i]

    fail.sort(key=lambda x: (-x[1], x[0]))

    answer = [x[0]+1 for x in fail]
    return answer