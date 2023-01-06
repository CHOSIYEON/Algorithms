def solution(emergency):
    rank = sorted(emergency, reverse=True)
    return [rank.index(i) + 1 for i in emergency]