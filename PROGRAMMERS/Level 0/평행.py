def solution(dots):
    # 1-2 / 3-4
    ans1 = (dots[0][0] - dots[1][0]) / (dots[0][1] - dots[1][1])
    ans2 = (dots[2][0] - dots[3][0]) / (dots[2][1] - dots[3][1])

    # 1-3 / 2-4
    ans3 = (dots[0][0] - dots[2][0]) / (dots[0][1] - dots[2][1])
    ans4 = (dots[1][0] - dots[3][0]) / (dots[1][1] - dots[3][1])

    # 1-4 / 2-3
    ans5 = (dots[0][0] - dots[3][0]) / (dots[0][1] - dots[3][1])
    ans6 = (dots[1][0] - dots[2][0]) / (dots[1][1] - dots[2][1])

    if ans1 == ans2 or ans3 == ans4 or ans5 == ans6:
        return 1

    return 0

###############################

from itertools import combinations

def solution(dots):
    # 기울기
    candidates = []
    for (x1, y1),(x2, y2) in combinations(dots, 2):
        candidates.append((y2 - y1, x2 - x1))

    for (x1, y1),(x2, y2) in combinations(candidates, 2):
        if y1 / x1 == y2 / x2:
            return 1
    return 0