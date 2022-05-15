def solution(s):
    answer = []
    tuples = []
    s = ''.join(s[1:-1].split('}')).split('{')

    for i in range(1, len(s)):
        temp = []
        arr = s[i].split(',')
        for j in arr:
            if j.isdigit():
                temp.append(j)
        tuples.append(temp)

    tuples.sort(key=lambda x: len(x))

    for i in range(len(tuples)):
        if i == 0:
            answer.append(int(tuples[i][0]))
        else:
            for j in tuples[i]:
                if not int(j) in answer:
                    answer.append(int(j))

    return answer

####################################################

def solution(s):
    answer = []
    s = eval(s.replace("{", "[").replace("}", "]"))

    s.sort(key=lambda x: len(x))

    for i in range(len(s)):
        if i == 0:
            answer.append(int(s[i][0]))
        else:
            for j in s[i]:
                if not int(j) in answer:
                    answer.append(int(j))

    return answer


#####################################################

def solution(s):
    answer = []
    s = eval(s.replace("{", "[").replace("}", "]"))

    s.sort(key=lambda x: len(x))

    for i in s:
        for j in i:
            if not int(j) in answer:
                answer.append(int(j))

    return answer