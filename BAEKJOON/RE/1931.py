import sys
input = sys.stdin.readline

n = int(input())
schedules = []
ans = 1

for i in range(n):
    line = list(map(int, input().split()))
    schedules.append(line)

schedules.sort(key=lambda x: (x[1], x[0]))
end = schedules[0][1]

for i in range(1, len(schedules)):
    if end <= schedules[i][0]:
        ans += 1
        end = schedules[i][1]

print(ans)
