import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = []
result = 0

for _ in range(n):
    heapq.heappush(cards, int(input()))

while len(cards) > 1:
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    temp = num1 + num2
    result += temp
    heapq.heappush(cards, temp)

print(result)