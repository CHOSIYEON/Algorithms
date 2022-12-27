def solution(num, total):
    answer = []

    if num % 2:
        center = total // num
        for i in range(num // 2 * (-1), num // 2 + 1):
            answer.append(center + i)
    else:
        center_sum = total // (num // 2)
        center = (center_sum - 1) // 2
        count = (num - 2) // 2

        for i in range(num):
            answer.append(center - count + i)

    return answer