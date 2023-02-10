def solution(s):
    answer = []

    for alpha in s:
        if not answer:
            answer.append(alpha)
        else:
            if answer[-1] == alpha:
                answer.pop()
            else:
                answer.append(alpha)

    return 1 if len(answer) == 0 else 0