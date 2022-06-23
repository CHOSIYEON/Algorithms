from itertools import permutations

def solution(k, dungeons):
    answer = -1
    candidates = list(permutations([x for x in range(len(dungeons))], len(dungeons)))

    for candidate in candidates:
        temp, cnt = k, 0
        for idx in candidate:
            if temp >= dungeons[idx][0]:
                temp -= dungeons[idx][1]
                cnt += 1
        answer = max(answer, cnt)

    return answer

## BFS
from collections import deque

def solution(k, dungeons):
    answer = -1
    queue = deque()
    queue.append((k, []))

    while queue:
        k, route = queue.popleft()
        for i in range(len(dungeons)):
            a, b = dungeons[i]
            if k >= a and i not in route:
                temp = route + [i]
                queue.append((k - b, temp))
            else:
                answer = max(answer, len(route))

    return answer