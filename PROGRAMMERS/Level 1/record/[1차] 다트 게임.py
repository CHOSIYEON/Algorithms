def solution(dartResult):
    answer = 0
    idx = 0
    scores = [0, 0, 0]

    for i in range(3):
        score = int(dartResult[idx])
        idx += 1
        if dartResult[idx] == '0':
            score = 10
            idx += 1
        if dartResult[idx] == 'S':
            score = score
        elif dartResult[idx] == 'D':
            score = pow(score, 2)
        elif dartResult[idx] == 'T':
            score = pow(score, 3)
        scores[i] = score
        idx += 1

        if idx >= len(dartResult):
            break

        if dartResult[idx] in ['*', '#']:
            if dartResult[idx] == '*':
                if i == 0:
                    scores[i] = score * 2
                else:
                    scores[i - 1] = scores[i - 1] * 2
                    scores[i] = score * 2
            else:
                scores[i] = score * (-1)

            idx += 1

    answer = sum(scores)
    return answer