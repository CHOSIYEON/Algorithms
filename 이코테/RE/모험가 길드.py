n = int(input())
people = list(map(int, input().split()))

people.sort()
ans = 0
temp = 0

for i in range(n):
    temp += 1
    if temp >= people[i]:
        ans += 1
        temp = 0

print(ans)