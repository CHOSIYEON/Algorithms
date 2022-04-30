def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        a = str(bin(i | j)[2:])
        a = a.zfill(n)
        a = a.replace('0', ' ')
        a = a.replace('1', '#')
        answer.append(a)

    return answer

# def make_map(arr):
#     data = []
#     for i in arr:
#         temp = ''
#         while i != 0:
#             temp += str(i % 2)
#             i //= 2
#
#         if len(temp) != len(arr):
#             temp += '0' * (len(arr) - len(temp))
#
#         data.append(temp)
#
#     return data
#
#
# def solution(n, arr1, arr2):
#     answer = [[-1] * n for _ in range(n)]
#     map1 = make_map(arr1)
#     map2 = make_map(arr2)
#
#     for i in range(n):
#         for j in range(n):
#             answer[i][n - j - 1] = int(map1[i][j]) + int(map2[i][j])
#
#     for i in range(n):
#         for j in range(n):
#             if answer[i][j] != 0:
#                 answer[i][j] = '#'
#             else:
#                 answer[i][j] = ' '
#
#         answer[i] = ''.join(answer[i])
#
#     return answer