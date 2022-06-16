def solution(A):
    # write your code in Python 3.6
    dict = {}

    for num in A:
        if num in dict.keys():
            dict[num] += 1
        else:
            dict[num] = 1

    for key, value in dict.items():
        if value % 2 != 0:
            return key