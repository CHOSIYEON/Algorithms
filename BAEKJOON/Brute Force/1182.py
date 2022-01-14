import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(1, n+1):
    combi = combinations(arr, i)
    for j in combi:
        cnt = sum(j)
        if cnt == s:
            ans += 1

print(ans)