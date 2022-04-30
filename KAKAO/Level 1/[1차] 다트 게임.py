def solution(dartResult):
    scores = []
    dartResult = dartResult.replace("10", "^")

    for dart in dartResult:
        if dart.isdigit():
            scores.append(int(dart))
        elif dart == "^":
            scores.append(10)
        elif dart == 'D':
            scores[-1] = pow(scores[-1], 2)
        elif dart == 'T':
            scores[-1] = pow(scores[-1], 3)
        elif dart == '*':
            scores[-1] *= 2
            if len(scores) > 1:
                scores[-2] *= 2
        elif dart == '#':
            scores[-1] *= (-1)

    return sum(scores)