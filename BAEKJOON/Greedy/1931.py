import sys
input = sys.stdin.readline

idx = 0
meetings = []
current = 0
result = 0

n = int(input())
for i in range(n):
    start, end = map(int, input().split())
    meetings.append([start, end])

meetings.sort(key=lambda x: (x[1], x[0]))

while idx < len(meetings):
    if current <= meetings[idx][0]:
        result += 1
        current = meetings[idx][1]
        idx += 1
    else:
        idx += 1

print(result)
