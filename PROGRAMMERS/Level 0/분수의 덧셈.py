from math import gcd
def solution(denum1, num1, denum2, num2):
    denum3, num3 = (denum1 * num2) + (denum2 * num1), num1 * num2
    return [denum3/gcd(denum3, num3), num3/gcd(denum3, num3)]

