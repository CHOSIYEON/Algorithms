def solution(n):
    answer = 0
    for i in range(2, n//2 + 1):
        if i * i == n:
            return 1
    return 2