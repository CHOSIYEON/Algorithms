import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

low, high = 1, max(arr)
result = 0

while low <= high:
    mid = (low+high) // 2
    cnt = 0
    for i in arr:
        cnt += i//mid
    if cnt >= k:
        result = mid
        low = mid + 1
    elif cnt < k:
        high = mid - 1

print(result)
