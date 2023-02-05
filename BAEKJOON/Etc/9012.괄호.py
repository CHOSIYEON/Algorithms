import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    data = input().strip()
    result = []

    for x in data:
        if x == '(':
            result.append(x)
        else:
            if result:
                result.pop()
            else:
                print("NO")
                break
    else:
        if result:
            print("NO")
        else:
            print("YES")