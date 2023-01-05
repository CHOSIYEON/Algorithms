def solution(s):
    answer, prev = 0, 0
    for i in s.split():
        if i == 'Z':
            answer -= prev
        else:
            answer += int(i)
            prev = int(i)
    return answer