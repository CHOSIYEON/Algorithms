from itertools import combinations

def isPrime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    candidates = list(combinations(nums, 3))

    for candidate in candidates:
        if isPrime(sum(candidate)):
            answer += 1

    return answer