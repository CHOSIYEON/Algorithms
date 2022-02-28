from itertools import permutations

def isPrime(number):
    if number < 2:
        return False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
    return True


def solution(numbers):
    length = len(numbers)
    numbers = list(numbers)
    answer = 0

    allNumbers = []

    for i in range(length):
        tmp = list(map(''.join, permutations(numbers, i + 1)))
        tmp = list(map(int, tmp))
        allNumbers += tmp

    allNumbers = set(allNumbers)

    for num in allNumbers:
        if isPrime(num):
            answer += 1

    return answer