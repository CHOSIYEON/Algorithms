import math
from itertools import permutations

def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1, 1):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    candidates = []

    for i in range(len(numbers)):
        candidates.extend(list(permutations(numbers, i + 1)))

    candidates = set([int(''.join(num)) for num in candidates])

    for candidate in candidates:
        if isPrime(candidate):
            answer += 1

    return answer