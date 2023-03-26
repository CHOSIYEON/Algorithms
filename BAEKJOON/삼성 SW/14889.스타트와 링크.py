import sys
input = sys.stdin.readline
from itertools import combinations

def cal(members):
    global answer
    start, link = 0, 0

    for i in range(n):
        for j in range(n):
            if i in members and j in members:
                start += data[i][j]

            if i not in members and j not in members:
                link += data[i][j]

    answer = min(answer, abs(start - link))

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
team = list(combinations(range(n), n // 2))
answer = 1e9

for i in range(len(team) // 2):
    cal(team[i])

print(answer)

## dfs

import sys
input = sys.stdin.readline

def cal():
    global answer, link
    start_sum, link_sum = 0, 0

    for i in range(n):
        if i not in start:
            link.append(i)

    for i in range(n // 2 - 1):
        for j in range(i + 1, n // 2):
            start_sum += data[start[i]][start[j]] + data[start[j]][start[i]]
            link_sum += data[link[i]][link[j]] + data[link[j]][link[i]]

    answer = min(answer, abs(start_sum - link_sum))
    link = []

def make_team(count):
    if count == n // 2:
        cal()
        return

    for i in range(count, n):
        if i in start:
            continue

        if len(start) > 0 and start[-1] > i:
            continue

        start.append(i)
        make_team(count + 1)
        start.pop()

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
start, link = [], []
answer = 1e9

make_team(0)
print(answer)
