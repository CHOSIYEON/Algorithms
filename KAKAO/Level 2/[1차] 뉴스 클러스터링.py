from collections import Counter


def solution(str1, str2):
    answer = 0
    total = 0
    set1 = []
    set2 = []

    for i in range(0, len(str1) - 1, 1):
        temp = str1[i:i + 2]
        if temp.isalpha():
            total += 1
            set1.append(temp.lower())

    for i in range(0, len(str2) - 1, 1):
        temp = str2[i:i + 2]
        if temp.isalpha():
            total += 1
            set2.append(temp.lower())

    if len(set1) == 0 and len(set2) == 0:
        return 65536

    set1, set2 = Counter(set1), Counter(set2)
    union_set = set1 + set2
    inter = 0

    for key in union_set.keys():
        if union_set[key] > 1:
            inter_cnt = min(set1[key], set2[key])
            total -= inter_cnt
            inter += inter_cnt

    if inter == 0:
        return 0

    answer = inter / total
    answer = int(str(answer * 65536 * 10000)[:5])

    return answer