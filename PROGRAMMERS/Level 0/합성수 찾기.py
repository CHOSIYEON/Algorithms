def get_divisors(n):
    divisior = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisior.append(i)
    if len(divisior) >= 3:
        return True
    return False


def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if get_divisors(i):
            answer += 1
    return answer


####

def get_divisors(n):
    return list(filter(lambda v: n % v == 0, range(1, n + 1)))


def solution(n):
    return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n + 1))))