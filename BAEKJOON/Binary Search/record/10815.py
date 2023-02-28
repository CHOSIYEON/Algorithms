import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr.sort()

def binary(i, arr):
    high = len(arr)-1
    low = 0
    mid = 0
    while low <= high:
        mid = (low + high) // 2

        if i == arr[mid]:
            return 1
        elif i > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return 0

for i in arr2:
    print(binary(i, arr), end=' ')



