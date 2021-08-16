n, p = map(int, input().split())
arr = []
visit = [0] * 2500000

arr.append(n)
visit[n] = 1

while True:
    sum = 0
    for i in list(map(int, str(n))):
        sum = sum + pow(i, p)

    if sum in arr and visit[sum] >= 3:
        break
    else:
        arr.append(sum)
        n = sum
        visit[n] += 1

print(visit.count(1))