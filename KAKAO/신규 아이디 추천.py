def solution(new_id):
    answer = ''
    check_close = True
    check = [i for i in range(97, 123)]
    temp = [i for i in range(48, 58)]
    check += temp
    check.append(45)
    check.append(46)
    check.append(95)

    new_id = new_id.lower()

    new = ''
    for i in new_id:
        if ord(i) in check:
            if ord(i) != 46:
                check_close = True
            if check_close:
                new += i
            if ord(i) == 46:
                check_close = False

    if ord(new[0]) == 46:
        new = new[1:]

    if len(new) >= 1:
        if ord(new[-1]) == 46:
            new = new[:-1]

    if len(new) < 1:
        new = 'a'

    if len(new) >= 16:
        new = new[:15]
        if ord(new[-1]) == 46:
            new = new[:-1]

    if len(new) <= 2:
        new += new[-1] * (3 - len(new))

    answer = new

    return answer