def dfs(node, visited, computers):
    visited[node] = True

    for i in range(len(computers)):
        if visited[i] == False and computers[node][i] == 1:
            visited[i] = True
            dfs(i, visited, computers)


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, visited, computers)

    return answer