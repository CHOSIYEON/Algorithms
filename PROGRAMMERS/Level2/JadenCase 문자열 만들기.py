def solution(s):
    answer = ''
    words = s.split(' ')

    for i in range(len(words)):
        words[i] = words[i].capitalize()

    return ' '.join(words)

##
def solution(s):
    answer = ''
    s.lower()
    s = list(s)
    flag = True

    for c in s:
        if flag:
            if c.isalpha():
                answer += c.upper()
                flag = False
                continue
            else:
                if c.isdigit():
                    flag = False

        if c.isalpha():
            answer += c.lower()
            continue

        if not c.isdigit():
            flag = True

        answer += c

    return answer