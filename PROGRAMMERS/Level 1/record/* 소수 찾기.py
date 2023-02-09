# 에라토스테네스의 체(Sieve of Eratosthenes)

def solution(n):
    answer = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in answer:
            answer -= set(range(2 * i, n + 1, i))

    return len(answer)