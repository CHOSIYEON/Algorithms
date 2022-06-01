# 정확성 통과, 효율성 통과 X
from itertools import product

def solution(n):
    answer = ''
    r, cnt = 0, 0

    if n == 1 or n == 2:
        return str(n)
    elif n == 3:
        return "4"

    while True:
        if cnt > n:
            print(r)
            break
        else:
            cnt += pow(3, r)
            r += 1

    idx = n - (cnt - pow(3, r - 1))
    answer = list(product([1, 2, 4], repeat=r - 1))[idx]
    answer = ''.join([str(x) for x in answer])
    return answer

# 정확성, 효율성 통과

def convert(n):
    tmp = ''

    while n:
        r = n % 3
        if r == 0:
            r = 3
            n -= 1
        tmp += str(r)
        n //= 3

    return tmp[::-1]

def solution(n):
    answer = convert(n)
    answer = answer.replace("3", "4")
    return answer