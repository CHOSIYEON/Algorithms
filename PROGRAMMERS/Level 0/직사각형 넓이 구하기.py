def solution(dots):
    dots.sort()
    return abs(dots[0][1] - dots[1][1]) * abs(dots[1][0] - dots[3][0])