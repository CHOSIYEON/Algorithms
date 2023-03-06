import sys
input = sys.stdin.readline
from itertools import combinations

def cal(chicken):
    distances = []
    for h in houses:
        temp = 1e9
        for c in chicken:
            temp = min(temp, abs(c[0] - h[0]) + abs(c[1] - h[1]))
        distances.append(temp)

    return sum(distances)

n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if info[i][j] == 1:
            houses.append((i, j))
        elif info[i][j] == 2:
            chickens.append((i, j))

selected_chicken = list(combinations(chickens, m))
answer = 1e9

for chicken in selected_chicken:
    answer = min(answer, cal(chicken))

print(answer)
