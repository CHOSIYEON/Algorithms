import sys
input = sys.stdin.readline

n = int(input())
data = [0] * 10000

for _ in range(n):
    data[int(input())-1] += 1

for i in range(10000):
    if data[i]:
        for j in range(data[i]):
            print(i+1)