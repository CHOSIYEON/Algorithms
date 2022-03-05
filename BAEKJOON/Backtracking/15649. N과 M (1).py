# from itertools import permutations
#
# n, m = map(int, input().split())
# arr = [str(i) for i in range(1, n+1)]
#
# answer = list(permutations(arr, m))
#
# for ans in answer:
#     print(' '.join(ans))

n, m = map(int, input().split())
visited = [False] * n
answer = []

def dfs():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(i+1)
            dfs()
            visited[i] = False
            answer.pop()

dfs()