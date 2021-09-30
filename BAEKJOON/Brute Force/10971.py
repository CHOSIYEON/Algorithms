from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
way = [i for i in range(n)]
way = permutations(way)
ans = []

def find_way(i):
    result = 0
    for j in range(n - 1):
        if cost[i[j]][i[j + 1]] != 0:
            result += cost[i[j]][i[j + 1]]
        else:
            return False
    if cost[i[-1]][i[0]] != 0:
        result += cost[i[-1]][i[0]]
    else:
        return False
    return result

for i in way:
    result = find_way(i)
    if result != False:
        ans.append(result)

print(min(ans))