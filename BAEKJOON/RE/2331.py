a, p = map(int, input().split())
arr = []
arr.append(a)
idx = 0

while True:
    num = 0
    for i in range(len(str(arr[idx]))):
        num = num + pow(int(str(arr[idx])[i]), p)

    if num in arr:
        print(arr.index(num))
        break
    else:
        arr.append(num)
        idx += 1
