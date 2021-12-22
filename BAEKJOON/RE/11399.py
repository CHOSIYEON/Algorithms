n = int(input())
people = list(map(int, input().split()))
ans = 0

people.sort()

for i in range(len(people)):
    ans += sum(people[:i+1])

print(ans)