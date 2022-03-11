from collections import deque

def solution(n, edges):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    distance = [0] * (n + 1)

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    queue = deque()
    queue.append([1, 0])
    visited[1] = True

    while queue:
        node, dis = queue.popleft()
        distance[node] = dis

        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                queue.append([i, dis + 1])

    answer = distance.count(max(distance))
    return answer

# 시간 초
# from collections import deque
#
#
# def solution(n, edges):
#     answer = 0
#     graph = [[0] * (n + 1) for _ in range(n + 1)]
#     visited = [0] * (n + 1)
#     distance = [0] * (n + 1)
#
#     for edge in edges:
#         graph[edge[0]][edge[1]] = 1
#         graph[edge[1]][edge[0]] = 1
#
#     queue = deque()
#     queue.append([1, 0])
#     visited[1] = True
#
#     while queue:
#         node, dis = queue.popleft()
#         distance[node] = dis
#
#         for i in range(n + 1):
#             if graph[node][i] == 1 and visited[i] == False:
#                 visited[i] = True
#                 queue.append([i, dis + 1])
#
#     answer = distance.count(max(distance))
#     return answer