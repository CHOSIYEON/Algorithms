def solution(d, budget):
    answer = 0
    d.sort()

    budget -= d[0]

    while budget >= 0:
        answer += 1

        if answer == len(d):
            break

        budget -= d[answer]

    return answer