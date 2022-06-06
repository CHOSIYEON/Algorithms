from collections import deque

def solution(priorities, location):
    answer = []
    queue = deque([(i, p) for i, p in enumerate(priorities)])

    priorities = deque(sorted(priorities, reverse=True))
    maxPriority = priorities.popleft()

    while queue:
        document, priority = queue.popleft()

        if priority == maxPriority:

            if document == location:
                return len(answer) + 1
            answer.append((document, priority))

            if priorities:
                maxPriority = priorities.popleft()
        else:
            queue.append((document, priority))

    return answer