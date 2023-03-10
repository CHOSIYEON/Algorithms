import sys
input = sys.stdin.readline
import heapq

n = int(input())
data = []
answer = 0

for _ in range(n):
    heapq.heappush(data, int(input()))

while len(data) > 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    answer += (a + b)
    heapq.heappush(data, a + b)

print(answer)