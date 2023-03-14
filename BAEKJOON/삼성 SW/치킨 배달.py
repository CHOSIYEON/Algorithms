import sys
input = sys.stdin.readline
from itertools import combinations

def cal(selected_chicken):
    global answer
    sum_distance = 0

    for house_x, house_y in houses:
        distance = 1e9
        for chicken_x, chicken_y in selected_chicken:
            distance = min(distance, abs(chicken_x - house_x) + abs(chicken_y - house_y))
        sum_distance += distance

    return sum_distance

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
houses = []
chickens = []
answer = 1e9

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            houses.append((i, j))
        elif data[i][j] == 2:
            chickens.append((i, j))

selected_chickens = list(combinations(chickens, m))

for selected_chicken in selected_chickens:
    answer = min(answer, cal(selected_chicken))

print(answer)
