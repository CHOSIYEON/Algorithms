from itertools import permutations

def check(user, banned_id):
    for u, b in zip(user, banned_id):
        if len(u) != len(b):
            return False

        for i in range(len(u)):
            if u[i] != b[i] and b[i] != '*':
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    candidates = list(permutations(user_id, len(banned_id)))

    for candidate in candidates:
        if check(candidate, banned_id):
            candidate = sorted(candidate)
            if candidate not in answer:
                answer.append(candidate)

    return len(answer)