from collections import deque

def solution(A, B):
    #     original = A
    #     A = deque(A)

    #     for i in range(len(A)):
    #         if ''.join(A) == B:
    #             return i

    #         A.rotate(1)

    #     return -1
    if A == B:
        return 0
    return len(A) - (A + A).find(B) if (A + A).find(B) != -1 else -1