from collections import deque

def solution(people, limit):
    idx, answer, weight = 0, 0, 0
    people.sort(reverse=True)
    people = deque(people)

    while len(people) >= 2:
        weight = 0
        answer += 1
        weight += people.popleft()

        while people:
            if weight + people[-1] <= limit:
                weight += people.pop()
            else:
                break

    if people:
        answer += 1

    return answer