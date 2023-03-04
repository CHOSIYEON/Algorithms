n = int(input())
arr = []

for _ in range(n):
    data = input().split()
    arr.append([data[0], int(data[1])])

arr.sort(key = lambda x: x[1])

for i in arr:
    print(i[0], end = ' ')