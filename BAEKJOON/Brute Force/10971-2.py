import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
routes = [i for i in range(n)]

per = permutations(routes)
ans = 10**10

for i in per:
    tmp = 0
    for j in range(n-1):
        if cost[i[j]][i[j+1]] != 0:
            tmp += cost[i[j]][i[j+1]]
        else:
            tmp = 0
            break

    if cost[i[-1]][i[0]] != 0 and tmp != 0:
        tmp += cost[i[-1]][i[0]]
        ans = min(ans, tmp)

print(ans)