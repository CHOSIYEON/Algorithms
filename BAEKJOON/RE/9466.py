import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000001)

def dfs(start):
    global result

    tmp.append(start)
    visited[start] = 1

    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
        else:
            if i in tmp:
                result += tmp[tmp.index(i):]


t = int(input())

for i in range(t):
    n = int(input())
    students = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    result = []

    for j in range(n):
        graph[j+1].append(students[j])

    for m in range(1, n+1):
        if not visited[m]:
            tmp = []
            dfs(m)

    print(n - len(result))


