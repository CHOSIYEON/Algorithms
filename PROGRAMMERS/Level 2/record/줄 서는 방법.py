import math

def solution(n, k):
    answer = []
    people = [x for x in range(1, n + 1)]

    while n:
        total = math.factorial(n) // n
        idx = k // total
        k %= total

        if not k:
            answer.append(people.pop(idx - 1))
        else:
            answer.append(people.pop(idx))

        n -= 1

    return answer

# 시간 초과
from itertools import permutations
def solution(n, k):
    answer = list(permutations([x for x in range(1, n+1)]))
    return answer[k-1]