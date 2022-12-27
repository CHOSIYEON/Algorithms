def solution(n, numlist):
    answer = []
    for num in numlist:
        if not num % n:
            answer.append(num)
    return answer

def solution(n, numlist):
    return [num for num in numlist if num % n == 0]