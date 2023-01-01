from collections import defaultdict

def solution(lines):
    answer = 0
    count = defaultdict(int)

    for line in lines:
        a, b = line[0] + 100, line[1] + 100
        for i in range(a, b):
            count[i] += 1
            if count[i] == 2:
                answer += 1

    return answer