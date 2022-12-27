def solution(my_str, n):
    return (list(map(lambda i : my_str[i:i+n], range(0, len(my_str), n))))