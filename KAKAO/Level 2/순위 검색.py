from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(infos, queries):
    answer = []
    people = defaultdict(list)

    for info in infos:
        info = info.split()
        score = int(info[-1])
        info = info[:-1]

        for i in range(5):
            combi = list(combinations([0, 1, 2, 3], i))
            for j in combi:
                temp = info[:]
                for m in j:
                    temp[m] = '-'
                people[''.join(temp)].append(score)

    for value in people.values():
        value.sort()

    for query in queries:
        query = query.split()
        q1, q2, q3, q4 = query[0], query[2], query[4], query[6]
        idx = bisect_left(people[q1 + q2 + q3 + q4], int(query[-1]))
        answer.append(len(people[q1 + q2 + q3 + q4]) - idx)

    return answer

# 정확성 통과, 효율성 통과 X
def solution(infos, queries):
    answer = []
    people = {}

    for i in range(len(infos)):
        info = infos[i].split()
        people[str(i) + ''.join(info[:-1])] = int(info[-1])

    for query in queries:
        query = query.split()
        count = 0
        q = []

        for i in range(4):
            if query[i * 2] != '-':
                q.append(query[i * 2])
            else:
                q.append('')

        for key in people.keys():
            if q[0] in key and q[1] in key and q[2] in key and q[3] in key:
                if people[key] >= int(query[-1]):
                    count += 1

        answer.append(count)

    return answer
