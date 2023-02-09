def solution(s):
    answer = False
    if s.lower().count('p') == s.lower().count('y'):
        answer = True
    return answer