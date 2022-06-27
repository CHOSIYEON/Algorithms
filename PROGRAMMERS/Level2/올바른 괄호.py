def solution(s):
    check = 0

    for c in s:
        if c == '(':
            check += 1
        else:
            check -= 1

        if check < 0:
            return False

    return True if not check else False