def factorial(n):
    fact = 1
    for i in range(2, n+1, 1):
        fact *= i
    return fact
def solution(balls, share):
    return factorial(balls) // (factorial(balls-share) *factorial(share))

###
import math
def solution(balls, share):
    return math.comb(balls, share)