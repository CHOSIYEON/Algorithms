import sys
input = sys.stdin.readline

n = int(input())
negative = []
positive = []
result = 0

for i in range(n):
    temp = int(input())
    if temp == 1:
        result += temp
    elif temp <= 0:
        negative.append(temp)
    else:
        positive.append(temp)


negative.sort()
positive.sort(reverse=True)

for i in range(0, len(negative), 2):
    if i+1 < len(negative):
        result = result + (negative[i] * negative[i+1])
    else:
        result += negative[i]

for i in range(0, len(positive), 2):
    if i+1 < len(positive):
        result = result + (positive[i] * positive[i+1])
    else:
        result += positive[i]

print(result)