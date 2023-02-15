def checkArr(p):
    q = []
    q.append(p[0])

    for i in range(1, len(p)):
        if len(q) > 0:
            if p[i] == ')' and q[-1] == '(':
                q.pop()
            else:
                q.append(p[i])
        else:
            q.append(p[i])

    if len(q) == 0:
        return True
    else:
        return False


def divide(p):
    cnt1, cnt2 = 0, 0

    for i in range(len(p)):
        if p[i] == '(':
            cnt1 += 1
        elif p[i] == ')':
            cnt2 += 1

        if cnt1 == cnt2:
            return i


def solution(p):
    answer = ''

    if len(p) == 0:
        return answer

    p = list(p)

    idx = divide(p)
    u = p[:idx + 1]
    v = p[idx + 1:]

    if checkArr(u):
        answer += ''.join(u)
        answer += solution(v)
    else:
        temp = '('
        temp += solution(v)
        temp += ')'
        u = u[1:len(u) - 1]

        for i in u:
            if i == '(':
                temp += ')'
            else:
                temp += '('

        answer += temp
    return answer

# def balanced_index(p):
#     count = 0
#     for i in range(len(p)):
#         if p[i] == '(':
#             count += 1
#         else:
#             count -= 1
#
#         if count == 0:
#             return i
#
#
# def check_proper(p):
#     count = 0
#     for i in p:
#         if i == '(':
#             count += 1
#         else:
#             if count == 0:
#                 return False
#             count -= 1
#
#     return True
#
#
# def solution(p):
#     answer = ''
#     if p == '':
#         return answer
#
#     index = balanced_index(p)
#     u = p[:index + 1]
#     v = p[index + 1:]
#
#     if check_proper(u):
#         answer += u + solution(v)
#     else:
#         answer = '('
#         answer += solution(v)
#         answer += ')'
#         u = list(u[1:-1])
#         for i in range(len(u)):
#             if u[i] == '(':
#                 u[i] = ')'
#             else:
#                 u[i] = '('
#
#         answer += ''.join(u)
#     return answer