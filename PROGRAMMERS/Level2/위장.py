from collections import defaultdict

def solution(clothes):
    answer = 1
    allClothes = defaultdict(list)

    for cloth in clothes:
        name, kind = cloth
        allClothes[kind].append(name)

    for key in allClothes.keys():
        answer *= (len(allClothes[key]) + 1)

    return answer - 1