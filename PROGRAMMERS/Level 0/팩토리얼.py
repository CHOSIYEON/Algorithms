def solution(n):
    answer, factorial = 1, 1

    while factorial <= n:
        answer += 1
        factorial *= answer

    return answer - 1