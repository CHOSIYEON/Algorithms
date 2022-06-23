def check(x, y, yellow):
    if 2 * x + 2 * y == x * y + 4 - yellow:
        return True
    return False


def solution(brown, yellow):
    sum_max = 2 + (brown // 2)

    for i in range(1, sum_max):
        if check(i, sum_max - i, yellow):
            return [sum_max - i, i]