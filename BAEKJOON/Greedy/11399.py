n = int(input())
time = list(map(int, input().split()))
time.sort()

result = []
temp = 0

for i in range(len(time)):
    if i != 0:
        temp = result[i-1] + time[i]
        result.append(temp)
    else:
        temp = temp + time[i]
        result.append(temp)

print(sum(result))