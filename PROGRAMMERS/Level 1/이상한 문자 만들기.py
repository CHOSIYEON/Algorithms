def solution(s):
    answer = ''
    list = s.split(' ')

    for i in range(len(list)):
        for j in range(len(list[i])):
            if j % 2 == 0:
                answer += list[i][j].upper()
            else:
                answer += list[i][j].lower()
        answer += ' '
    return answer[:-1]