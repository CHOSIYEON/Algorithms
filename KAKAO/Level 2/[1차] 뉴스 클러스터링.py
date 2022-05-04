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

    set1, set2 = Counter(set1), Counter(set2)

    inter = list((set1 & set2).elements())
    union = list((set1 | set2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
