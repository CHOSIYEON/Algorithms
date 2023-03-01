def check(num):
    start, end = 0, n-1

    while start <= end:
        mid = (start + end) // 2

        if cards[mid] == num:
            return True
        elif cards[mid] > num:
            end = mid - 1
        else:
            start = mid + 1

    return False

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

cards.sort()

for i in arr:
    if check(i):
        print("1", end=' ')
    else:
        print("0", end=' ')