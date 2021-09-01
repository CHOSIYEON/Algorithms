import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

low, high = 1, arr[-1] - arr[0]
mid = 0
result = 0

while low <= high:
    mid = (low+high) // 2
    idx = 0
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] >= arr[idx] + mid:
            cnt += 1
            idx = i
    if cnt >= c:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
