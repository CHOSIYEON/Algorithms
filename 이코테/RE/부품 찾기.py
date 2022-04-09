n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

def binary_search(start, end, target):
    while start <= end:
        mid = (start+end) // 2

        if arr1[mid] == target:
            return "yes"
        elif arr1[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return "no"


for i in arr2:
    print(binary_search(0, n-1, i), end=' ')