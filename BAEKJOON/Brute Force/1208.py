import sys
from itertools import combinations
from collections import defaultdict
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

arr1 = arr[:n//2]
arr2 = arr[n//2:]

arr1_sum = defaultdict(int)
arr2_sum = defaultdict(int)
arr1_sum[0] = 1
arr2_sum[0] = 1

for i in range(1, len(arr1)+1):
    for j in combinations(arr1, i):
        arr1_sum[sum(j)] += 1

for i in range(1, len(arr2)+1):
    for j in combinations(arr2, i):
        arr2_sum[sum(j)] += 1

arr1_key = sorted(arr1_sum.keys())
arr2_key = sorted(arr2_sum.keys())

left = 0
right = len(arr2_key) - 1

while left < len(arr1_key) and right >= 0:
    if arr1_key[left] + arr2_key[right] > s:
        right -= 1
    elif arr1_key[left] + arr2_key[right] < s:
        left += 1
    elif arr1_key[left] + arr2_key[right] == s:
        ans += (arr1_sum[arr1_key[left]] * arr2_sum[arr2_key[right]])
        left += 1
        right -= 1

if s == 0:
    ans -= 1

print(ans)
