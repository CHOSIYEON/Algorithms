def solution(polynomial):
    answer = ''
    variable, constant = 0, 0
    for p in polynomial.split('+'):
        p = p.strip()
        if 'x' in p:
            if len(p) > 1:
                variable += int(p[:-1])
            else:
                variable += 1
        else:
            constant += int(p)

    if variable > 1:
        answer += str(variable) + 'x'
    elif variable == 1:
        answer += 'x'

    if variable >= 1:
        if constant > 0:
            answer += ' + ' + str(constant)
    else:
        if constant > 0:
            answer += str(constant)

    return answer