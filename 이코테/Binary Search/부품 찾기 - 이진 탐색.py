n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr.sort()

start = 0
end = len(arr) - 1

def binary_search(start, end, target):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return "yes"
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"

for target in arr2:
    print(binary_search(start, end, target), end= ' ')
