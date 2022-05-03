def separate(arr):
    var = 0
    for idx in range(len(arr)):
        if arr[idx] == '(':
            var += 1
        elif arr[idx] == ')':
            var -= 1

        if var == 0:
            return idx


def isRight(u):
    var = 0
    for idx in range(len(u)):
        if u[idx] == '(':
            var += 1
        elif u[idx] == ')':
            var -= 1

        if var < 0:
            return False

    return True


def solution(p):
    answer = ''

    if len(p) == 0:
        return ''

    idx = separate(p)
    u, v = p[:idx + 1], p[idx + 1:]

    if isRight(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = u[1:len(u) - 1]

        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('

    return answer

# def balanced_arr(arr):
#     var = 0
#     for idx in range(len(arr)):
#         if arr[idx] == '(':
#             var += 1
#         elif arr[idx] == ')':
#             var -= 1
#
#         if var == 0:
#             return idx
#
#
# def correct_arr(arr):
#     var = 0
#     for idx in range(len(arr)):
#         if arr[idx] == '(':
#             var += 1
#         elif arr[idx] == ')':
#             var -= 1
#
#         if var < 0:
#             return False
#
#     return True
#
#
# def solution(p):
#     answer = ''
#
#     if len(p) == 0:
#         return answer
#
#     idx = balanced_arr(p)
#     u, v = p[:idx + 1], p[idx + 1:]
#
#     if correct_arr(u):
#         answer += u
#         answer += solution(v)
#     else:
#         temp = '('
#         temp += solution(v)
#         temp += ')'
#         u = u[1:len(u) - 1]
#
#         for i in u:
#             if i == '(':
#                 temp += ')'
#             else:
#                 temp += '('
#
#         answer += temp
#
#     return answer