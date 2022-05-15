from itertools import permutations

def solution(expressions):
    answer = -1e9
    priorites = list(permutations(['+', '-', '*']))

    for priority in priorites:
        last = []
        first = expressions.split(priority[0])

        for expression in first:
            second = expression.split(priority[1])
            second = [str(eval(x)) for x in second]
            last.append(priority[1].join(second))

        last = [str(eval(x)) for x in last]
        last = priority[0].join(last)
        answer = max(answer, abs(eval(last)))

    return answer