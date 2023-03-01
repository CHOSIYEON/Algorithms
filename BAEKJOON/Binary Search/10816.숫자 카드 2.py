from collections import defaultdict

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

count = defaultdict(int)

for card in cards:
    count[card] += 1

for i in arr:
    print(count[i], end=' ')
