def solution(order):
    answer = 0
    for num in list(map(int, list(str(order)))):
        if num in [3, 6, 9]:
            answer += 1
    return answer

def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))