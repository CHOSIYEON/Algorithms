from collections import deque

def solution(A, K):
    # write your code in Python 3.6
    A = deque(A)
    A.rotate(K)
    return [x for x in A]