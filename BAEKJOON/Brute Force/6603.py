import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    tmp = list(map(int, input().split()))
    k = tmp.pop(0)

    if k == 0:
        break

    combi = combinations(tmp, 6)

    for i in combi:
        for j in i:
            print(j, end=' ')
        print()

    print()