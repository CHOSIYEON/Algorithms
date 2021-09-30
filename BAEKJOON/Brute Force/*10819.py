from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

per = permutations(arr)
ans = []

for i in per:
    result = 0
    for j in range(len(i)-1):
        result += abs(i[j]-i[j+1])
    ans.append(result)

print(max(ans))