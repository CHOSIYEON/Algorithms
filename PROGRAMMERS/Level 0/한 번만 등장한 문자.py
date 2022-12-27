def solution(s):
    answer = ''
    for word in set(s):
        if s.count(word) == 1:
            answer += word
    return ''.join(sorted(answer))