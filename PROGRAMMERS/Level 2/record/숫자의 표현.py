def solution(n):
    answer = 1

    for i in range(1, n // 2 + 1):
        sum_value = 0
        for j in range(i, n):
            sum_value += j
            if sum_value > n:
                break
            elif sum_value == n:
                answer += 1
                break

    return answer