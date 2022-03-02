from collections import defaultdict


def solution(tickets):
    answer = []

    routes = defaultdict(list)

    for key, value in tickets:
        routes[key].append(value)

    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())

    answer = path[::-1]
    return answer