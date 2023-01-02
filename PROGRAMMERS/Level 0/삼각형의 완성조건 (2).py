def solution(sides):
    #     # 가장 긴 변이 sides 중 하나일 때
    #     answer += (max(sides) - max(sides) + min(sides))

    #     # 가장 긴 변이 나머지 하나 값일 때
    #     answer += (sum(sides) - max(sides) - 1)
    return sum(sides) + min(sides) - max(sides) - 1