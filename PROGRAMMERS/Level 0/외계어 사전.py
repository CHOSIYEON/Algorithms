from itertools import permutations

def solution(spell, dic):
    candidates = list(permutations(spell, len(spell)))

    for candidate in candidates:
        if ''.join(candidate) in dic:
            return 1
    return 2