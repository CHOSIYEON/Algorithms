import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

per = permutations(arr)
ans = 0

for i in per:
    tmp = 0
    for j in range(n-1):
        tmp += abs(i[j]-i[j+1])
    ans = max(ans, tmp)

print(ans)

