from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    candidates = list(permutations(dist, len(dist)))

    for i in range(len(weak)):
        weak.append(weak[i] + n)

    for start in range(length):
        for candidate in candidates:
            count = 1
            possible = weak[start] + candidate[count - 1]

            for idx in range(start, start + length):
                if possible < weak[idx]:
                    count += 1

                    if count > len(dist):
                        break
                    possible = weak[idx] + candidate[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1

    return answer