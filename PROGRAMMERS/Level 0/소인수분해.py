def solution(n):
    answer = []
    d = 2

    while d <= n:
        if n % d == 0:
            n /= d
            answer.append(d)
        else:
            d += 1
    return sorted(list(set(answer)))