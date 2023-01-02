def solution(my_string):
    answer = 0
    tmp = ''

    for w in my_string:
        if w.isalpha() and tmp != '':
            answer += int(tmp)
            tmp = ''
        if w.isdigit():
            tmp += w

    if tmp != '':
        answer += int(tmp)
    return answer

############################
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())