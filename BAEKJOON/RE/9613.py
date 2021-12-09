import sys
input = sys.stdin.readline

def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

t = int(input())

for n in range(t):
    arr = list(map(int, input().split()))
    ans = []
    arr.pop(0)

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            ans.append(gcd(arr[i], arr[j]))

    print(sum(ans))
