def first(target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == 0 or target > data[mid - 1]) and data[mid] == target:
        return mid
    elif data[mid] >= target:
        return first(target, start, mid - 1)
    else:
        return first(target, mid + 1, end)

def last(target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == n - 1 or data[mid + 1] > target) and data[mid] == target:
        return mid
    elif data[mid] > target:
        return last(target, start, mid - 1)
    else:
        return last(target, mid + 1, end)

n, x = map(int, input().split())
data = list(map(int, input().split()))
start, end = 0, len(data) - 1
answer = 0

first_index = first(x, start, end)
last_index = last(x, start, end)

if first_index == None:
    print(-1)
else:
    print(last_index - first_index + 1)


# 7 2
# 1 1 2 2 2 2 3
# 7 4
# 1 1 2 2 2 2 3