def solution(i, j, k):
    return sum(list(map(lambda x: str(x).count(str(k)), [x for x in range(i, j+1)])))