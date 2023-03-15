import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
b, c = map(int, input().split())
answer = n

for i in data:
    i -= b

    if i > 0:
        if i % c == 0:
            answer += i // c
        else:
            answer += (i // c + 1)

print(int(answer))



