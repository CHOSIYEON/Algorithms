import sys
input = sys.stdin.readline

n = input()
li = list(map(int, input().split()))
sum = 0

for i in li:
    for j in range(i-1, 1, -1):
        if i % j == 0:
            sum += 1
            break

print(len(li) - sum - li.count(1))