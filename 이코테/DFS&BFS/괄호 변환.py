def seperate(p):
    c1, c2 = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            c1 += 1
        else:
            c2 += 1

        if c1 == c2:
            return i


def isRight(u):
    check = 0
    for i in range(len(u)):
        if u[i] == '(':
            check += 1
        else:
            check -= 1

        if check < 0:
            return False

    return True


def solution(p):
    answer = ''

    if len(p) == 0:
        return ''

    idx = seperate(p)
    u, v = p[:idx + 1], p[idx + 1:]

    if isRight(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = u[1:len(u) - 1]

        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('

    return answer