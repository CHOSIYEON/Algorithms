def solution(my_string, n):
    return ''.join(list(map(lambda x: x*n, my_string)))