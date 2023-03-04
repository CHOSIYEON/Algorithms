def solution(n, stages):
    answer = []
    data = [0] * (n + 2)

    for stage in stages:
        data[stage] += 1

    for i in range(1, n + 1):
        if data[i] == 0:
            answer.append((0, i))
        else:
            answer.append((data[i] / sum(data[i:]), i))

    answer.sort(key=lambda x: (-x[0], x[1]))

    return [answer[i][1] for i in range(n)]