def solution(d, budget):
    answer = 0
    d = sorted(d)

    for i in range(len(d)):
        temp = budget - d[i]
        if temp >= 0:
            budget -= d[i]
            answer += 1
        else:
            break

    return answer