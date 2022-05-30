def solution(progresses, speeds):
    answer = []

    while len(progresses) > 1:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        for i in range(len(progresses)):
            if progresses[i] < 100:
                break

        if i != 0:
            progresses = progresses[i:]
            answer.append(i)

    return answer

solution([93, 30, 55], [1, 30, 5])