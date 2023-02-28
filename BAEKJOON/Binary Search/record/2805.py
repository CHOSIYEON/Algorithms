import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
low, high = 1, max(arr)
result = 0

while low <= high:
    mid = (low + high) // 2
    tree = 0
    for i in arr:
        if i >= mid:
            tree += (i-mid)
    if tree >= m:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)