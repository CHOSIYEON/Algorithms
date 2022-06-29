# https://shoark7.github.io/programming/algorithm/tower-of-hanoi

def hanoi(n, start, to, via):
    if n == 1:
        answer.append([start, to])
    else:
        hanoi(n - 1, start, via, to)
        answer.append([start, to])
        hanoi(n - 1, via, to, start)


def solution(n):
    global answer
    answer = []
    hanoi(n, 1, 3, 2)
    return answer