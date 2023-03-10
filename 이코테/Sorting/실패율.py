def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            answer.append((i, 0))
        else:
            answer.append((i, count / length))

        length -= count

    answer.sort(key=lambda x: -x[1])
    answer = [i[0] for i in answer]

    return answer