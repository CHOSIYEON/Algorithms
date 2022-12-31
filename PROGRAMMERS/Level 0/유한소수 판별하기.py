def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def factorization(x):
    divisors = []
    d = 2
    while d <= x:
        if x % d == 0:
            divisors.append(d)
            x = x / d
        else:
            d = d + 1
    return divisors


def solution(a, b):
    b //= get_gcd(a, b)
    divisors = factorization(b)

    for divisor in divisors:
        if not divisor in [2, 5]:
            return 2

    return 1

###########################################

from math import gcd


def solution(a, b):
    b //= gcd(a, b)

    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    return 1 if b == 1 else 2
