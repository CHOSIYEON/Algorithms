import math

def convert(num, base):
    tmp = '0123456789ABCDEF'
    q, r = divmod(num, base)

    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]

def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def solution(n, k):
    answer = 0

    arr = convert(n, k).split('0')
    arr = [int(x) for x in arr if x != '']

    for num in arr:
        if isPrime(num):
            answer += 1

    return answer