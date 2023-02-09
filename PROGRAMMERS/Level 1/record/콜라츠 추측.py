def solution(num):
    answer = 0
    count = 0
    while num != 1:
        count += 1
        answer = count
        if count > 500:
            answer = -1
            break
        if num % 2 == 0:
            num = num/2
        else:
            num = num * 3 + 1
    return answer