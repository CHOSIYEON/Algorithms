import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    arr = list(input().rstrip())
    temp = []
    for j in arr:
        if len(temp) >= 1:
            if temp[-1] == '(' and j == ')':
                temp.pop()
            else:
                temp.append(j)
        else:
            temp.append(j)
    if len(temp) == 0:
        print("YES")
    else:
        print("NO")