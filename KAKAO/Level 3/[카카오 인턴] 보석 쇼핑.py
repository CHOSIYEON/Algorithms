from collections import Counter
def solution(gems):
    answer = []
    gemCnt = len(set(gems))
    gemList = Counter()
    start = 0

    for end in range(len(gems)):
        gemList[gems[end]] += 1

        while len(gemList) == gemCnt:
            answer.append((start + 1, end + 1))
            gemList[gems[start]] -= 1

            if not gemList[gems[start]]:
                del gemList[gems[start]]

            start += 1

    return sorted(answer, key=lambda x: (x[1] - x[0]))[0]