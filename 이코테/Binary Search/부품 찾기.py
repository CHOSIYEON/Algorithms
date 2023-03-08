n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    start, end = 0, len(arr1) - 1
    answer = False

    while start <= end:
        mid = (start + end) // 2

        if arr1[mid] == i:
            answer = True
            break
        elif arr1[mid] > i:
            end = mid - 1
        else:
            start = mid + 1

    if answer:
        print("yes")
    else:
        print("no")
