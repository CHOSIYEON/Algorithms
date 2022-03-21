import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    temp = int(input())
    if temp == 0:
        if len(q) > 0:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, temp)